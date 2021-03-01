import loan_pb2 as pb2

class Repayment:
    def __init__(self, term, principal, interest, total, date, status, email, loan_no):
      self.term = term
      self.principal = principal
      self.total = total
      self.interest = interest
      self.date = date
      self.status = status
      self.email = email
      self.loan_no = loan_no

def get_repayment_item(loan):
  item = pb2.repaymentItem()
  item.term = loan.term
  item.principal = loan.principal
  item.interest = loan.interest
  item.total = loan.total
  item.date = loan.date
  item.status = loan.status
  item.email = loan.email
  item.loan_no = loan.loan_no
  return item

def to_json(loans):
  data = []
  for item in loans:
    obj = {}
    obj['term'] = item.term
    obj['principal'] = item.principal
    obj['interest'] = item.interest
    obj['date'] = item.date
    obj['status'] = item.status
    obj['total'] = item.total
    obj['email'] = item.email
    obj['loan_no'] = item.loan_no
    data.append(obj)
  return data

def from_json(data):
  loans = []
  for i in range(len(data)):
      item = Repayment(data[i]['term'], data[i]['principal'], data[i]['interest'], data[i]['total'], data[i]['date'], data[i]['status'], data[i]['email'], data[i]['loan_no'])
      loans.append(item)
  return loans
