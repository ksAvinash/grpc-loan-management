import grpc
import logging
from datetime import timedelta, date
from concurrent import futures

import db
import helper
import repayment
import loan_pb2 as pb2
import loan_pb2_grpc as pb2_grpc
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class MyLoanService(pb2_grpc.QuikLoanerServicer):
    def __init__(self):
        self.loans = db.restoreRepayments()
        logging.info('restored active repayments: ' + str(len(self.loans)))

    def save_loan(self, request, context):
        logging.info('received new loan request: '+ str(request))
        loan_no = helper.get_loan_number()
        logging.info('generated new loan number: ' + loan_no)
        interest = (request.loan_amount * request.interest_rate) / (100 * request.repayment_terms)
        term_amount = request.loan_amount / request.repayment_terms
        logging.info('interest per term: ' + str(interest))
        logging.info('term amount: '+ str(term_amount))
        for i in range(request.repayment_terms):
            _date = date.today() + timedelta(days=i)
            item = repayment.Repayment(i + 1, term_amount, interest, request.loan_amount, _date.strftime("%b %d %Y"), 'not-paid', request.email, loan_no)
            self.loans.append(item)
        db.saveRepayments(self.loans)
        logging.info('total active repayments: ' + str(len(self.loans)))
        resp = pb2.createLoanResponse()
        resp.success = True
        return resp

    def show_repayments(self, request, context):
        logging.info('received show repayments request: ' + str(request))
        resp = pb2.showRepaymentResponse()
        for loan in self.loans:
            if loan.email == request.email:
                item = repayment.get_repayment_item(loan)
                resp.items.append(item)
        logging.info('found user repayments: ' + str(len(resp.items)))
        return resp

    def make_repayment(self, request, context):
        logging.info('received make repayment request: ' + str(request))
        found = False
        for i in range(len(self.loans)):
            loan = self.loans[i]
            if loan.email == request.email and loan.term == request.term and loan.total == request.amount:
                found = True
                self.loans[i].status = 'paid'
                db.saveRepayments(self.loans)
                logging.info('successfully paid repayment amount for: '+request.email+ ' : ' + str(request.term) + ' : '+ str(request.amount))
                break
        resp = pb2.makeRepaymentResponse()
        if found:
            resp.success = True
        else:
            resp.success = False
        return resp


if __name__ == '__main__':
    logging.info('starting the server on port 50055..')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_QuikLoanerServicer_to_server(MyLoanService(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()