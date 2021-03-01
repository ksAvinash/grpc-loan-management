import grpc
import loan_pb2 as pb2
import loan_pb2_grpc as pb2_grpc

import helper
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class LoanServer:
  def __init__(self):
    self.channel = grpc.insecure_channel('localhost:50055')
    self.stub = pb2_grpc.QuikLoanerStub(self.channel)
  
  def new_loan(self, email, interest_rate, repayment_terms, loan_amount):
    req = pb2.createLoanRequest(email=email, interest_rate=interest_rate, repayment_terms=repayment_terms, loan_amount=loan_amount)
    resp = self.stub.save_loan(req)
    if resp.success:
      logging.info('new loan saved successfully')
    else:
      logging.info('error saving new loan')

  def show_repayments(self, email):
    req = pb2.showRepaymentRequest(email=email)
    resp = self.stub.show_repayments(req)
    helper.log_repayments(resp.items)

  def make_repayment(self, email, term, amount):
    req = pb2.makeRepaymentRequest(email=email, term=term, amount=amount)
    resp = self.stub.make_repayment(req)
    if resp.success:
      logging.info('repayment successful')
    else:
      logging.info('repayment failed')


if __name__ == '__main__':
  loanserver = LoanServer()
  while True:
    logging.info('choose the action to perform')
    logging.info('1. New Loan')
    logging.info('2. Show Repayments')
    logging.info('3. Make RePayment')
    choice = input()

    if choice == 1:
      logging.info('provide loan details in the format: email <> interest_rate <> repayment_terms <> loan_amount')
      request = helper.validate_loan_request(choice, raw_input())
      if not request['success']:
        logging.error('invalid new loan request')
      else:
        loanserver.new_loan(request['email'], request['interest_rate'], request['repayment_terms'], request['loan_amount'])


    elif choice == 2:
      logging.info('provide user details in the format: email')
      request = helper.validate_loan_request(choice, raw_input())
      if not request['success']:
        logging.error('invalid show repayment')
      else:
        loanserver.show_repayments(request['email'])


    elif choice == 3:
      logging.info('provide repayment details in the format: email <> term <> amount')
      request = helper.validate_loan_request(choice, raw_input())
      if not request['success']:
        logging.error('invalid repayment request')
      else:
        loanserver.make_repayment(request['email'], request['term'], request['amount'])

    else:
      logging.error('invalid choice, try again')
      break
    