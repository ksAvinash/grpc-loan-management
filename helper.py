import random
import string

# generate 10 digit random loan number
def get_loan_number():
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


# perform basic request validations, can be enhanced to use request validators
def validate_loan_request(choice, request):
  resp = {}
  resp['success'] = True
  request = request.split(' ')
  if choice == 1:
    if len(request) != 4:
      resp['success'] = False
    else:
      resp['email'] = request[0]
      resp['interest_rate'] = float(request[1])
      resp['repayment_terms'] = int(request[2])
      resp['loan_amount'] = int(request[3])
  elif choice == 2:
    resp['email'] = request[0]
  elif choice == 3:
    if len(request) != 3:
      resp['success'] = False
    else:
      resp['email'] = request[0]
      resp['term'] = int(request[1])
      resp['amount'] = int(request[2])
  return resp


# library textable is used to ouput repayments in tabular format
def log_repayments(items):
  rows = []
  rows.append([ 'email', 'loan_no', 'term', 'principal', 'interest', 'total', 'date', 'status'])
  for item in items:
    repayment = [item.email, item.loan_no, item.term, item.principal, item.interest, item.total, item.date, item.status]
    rows.append(repayment)
  from texttable import Texttable
  t = Texttable()
  t.add_rows(rows)
  print(t.draw())