import json
import repayment


filename = 'repayments.json'

def saveRepayments(loans):
  # can be replaced with actual data-db to save loans
  data = repayment.to_json(loans)
  with open(filename, 'w') as outfile:
    json.dump(data, outfile)

def restoreRepayments():
  # can be replaced with actual data-db to restore all loans onto the server
  with open(filename) as json_file:
    data = json.load(json_file)
    return repayment.from_json(data)