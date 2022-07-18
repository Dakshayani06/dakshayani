#### CALL INCOME STATEMENT API ####
# This demo calls for income statement API from https://www.alphavantage.co/
import json
import requests

api_key = "demo"
url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey={api_key}"
response = requests.get(url)
##print(response)
income = response.json()
##print(income)
# The api data in this demo is more nested than demo 1

# When data is too nested, use json module to provide better readability
# indent 4 whitespace in annualReports key provide better readability
print(json.dumps(income, indent=4))

# Try to write data as txt or csv on your own after that.

# test
a=10