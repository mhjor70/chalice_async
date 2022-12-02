# app.py
# import our requirements
import json
import time

import requests
from chalice import Chalice

# initialize our response list return variable
return_list = []

## Out list of api's to gather data from
list_of_urls = [
    "http://universities.hipolabs.com/search?country=United+States",
    "http://universities.hipolabs.com/search?country=Australia",
    "http://universities.hipolabs.com/search?country=United+Kingdom",
    "http://universities.hipolabs.com/search?country=New+Zeland",
    "http://universities.hipolabs.com/search?country=Germany",
    "http://universities.hipolabs.com/search?country=Italy",
    "http://universities.hipolabs.com/search?country=Spain",
    "http://universities.hipolabs.com/search?country=France",
    "http://universities.hipolabs.com/search?country=Sweden",
    "http://universities.hipolabs.com/search?country=Norway",
    "http://universities.hipolabs.com/search?country=Denmark",
    "http://universities.hipolabs.com/search?country=Finland",
    "http://universities.hipolabs.com/search?country=Switzerland",
    "http://universities.hipolabs.com/search?country=Poland",
    "http://universities.hipolabs.com/search?country=Belgium",
    "http://universities.hipolabs.com/search?country=Romania",
    "http://universities.hipolabs.com/search?country=Hungary",
    "http://universities.hipolabs.com/search?country=India",
    "http://universities.hipolabs.com/search?country=Mexico",
    "http://universities.hipolabs.com/search?country=Brazil",
    "http://universities.hipolabs.com/search?country=Canada",
    "http://universities.hipolabs.com/search?country=Indonesia",
    "http://universities.hipolabs.com/search?country=China",
]


def download_site(url, session):
    tempReturnList = []
    with session.get(url) as response:
        tempReturnList = response.json()
    return tempReturnList


def download_all_sites(sites):
    result_list = []
    with requests.Session() as session:
        for url in sites:
            tempResult = download_site(url, session)
            result_list.append(tempResult)
    return result_list


app = Chalice(app_name="restcollector")
# uses requests to gather the information from the api and return it
@app.route("/")
def index():
    resultSet = []
    print("Starting Timer...")
    startTime = time.time()
    resultSet = list(download_all_sites(list_of_urls))
    for countries in resultSet:
        for colleges in countries:
            return_list.append(colleges["alpha_two_code"] + ":" + colleges["name"])
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f" Total Execution time from invocation: {elapsedTime}")
    return {"response": f"{return_list}"}
