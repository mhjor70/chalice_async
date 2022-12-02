# app.py
# import our requirements
import json
import time

from chalice import Chalice
from requests_futures.sessions import FuturesSession

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


def getResponse(urls):
    session = FuturesSession()
    resultTemp = {}
    respTemp = {}
    for i in range(0, len(urls)):
        # create a good key for our dictionary
        tvar = urls[i].split("=")
        tvar = tvar[1]
        keyval = tvar.replace("+", "_")
        # process our results which will fire and return
        resultTemp[keyval] = session.get(urls[i])
        # build the dictionary of our results as they return
        respTemp[keyval] = resultTemp[keyval].result().json()
    return respTemp


app = Chalice(app_name="restcollector")
# uses requests to gather the information from the api and return it
@app.route("/")
def index():
    # initialize our response list return variable
    return_list = []
    resultSet = []
    # start the Time
    print("Starting Timer...")
    startTime = time.time()
    resultSet = getResponse(list_of_urls)
    for country in resultSet:
        for key in resultSet[country]:
            firstval = key["alpha_two_code"]
            collegeName = key["name"]
            return_list.append(str(firstval) + ":" + str(collegeName))
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f" Total Execution time from invocation: {elapsedTime}")
    return {"response": f"{return_list}"}
