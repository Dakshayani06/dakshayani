#### DEMO ON API ####
# This demo will focus on calling web API from https://www.alphavantage.co/
# Connect to web API provide many useful purpose to tap on real world data

#### INSTALL AND IMPORT REQUESTS MODULE ####
# Install "requests" module under terminal: pip install requests
# Import requests module
from asyncore import write
from pathlib import Path
import csv
from sys import float_info
from urllib import response
import requests

#### API INFO ####
# Obtain an API key
api_key = "demo"
# To call for a specific API, refer to the url from https://www.alphavantage.co/documentation/
# For example, to find out the GDP data, refer to the Economic Indicators documentation
# The url here is inflation data under Economic Indicators
url = f"https://www.alphavantage.co/query?function=INFLATION&apikey={api_key}"

#### GET RESPONSE FROM API ####
# use get method from requests on the api url

response = requests.get(url)

# reponse code 200 means a successful api call

#print(response)
# use json method from requests to get data, print to show data

##print(response.json())

# assign variable to data

inflation = response.json()
##print(inflation.keys())

# extract inflation value from the key: "data"

# let's write data to a csv file!
# create a csv in current folder
fp = Path.cwd()/"inflation.csv"
fp.touch()

# context manager to open file in "write" mode
with fp.open(mode= "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    # write header
writer.writerow(["Year","Inflation"])
    # iterate over data to write data in csv file
for data in inflation["data"]:
    writer.writerow([data["date"],data ["value"]])

