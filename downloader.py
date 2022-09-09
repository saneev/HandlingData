import json
import requests
from pymongo import MongoClient
from requests.auth import HTTPBasicAuth


def getData():
    '''
    Fetches data from the API Endpoint with the parameters in the payload Dict

    '''

    # Creating parameters for queries

    payload_leisure = {'area': '35', 'pertypdesc': 'Annual', 'indcode': '1026', '$limit': '30000'}
    payload_realEstate = {'area': '35', 'pertypdesc': 'Annual', 'indcode': '531', '$limit': '30000'}
    payload_information = {'area': '35', 'pertypdesc': 'Annual', 'indcode': '51', '$limit': '30000'}

    # Querying responses as per the parameters
    # Queries Douglas County, Annual, Informaiton/ Leisure and Hospitality/ Real Estate Informaiton

    response_leisure = requests.get("https://data.colorado.gov/resource/cjkq-q9ih.json", auth=basic, params=payload_leisure)
    response_realEstate = requests.get("https://data.colorado.gov/resource/cjkq-q9ih.json", auth=basic, params=payload_realEstate)
    response_information = requests.get("https://data.colorado.gov/resource/cjkq-q9ih.json", auth=basic, params=payload_information)

    return response_leisure.json(), response_realEstate.json(), response_information.json()


def dataWrite(db, db_collection, responses):
    '''

    Writes data fetched from API Endpoint to MongoDB Atlas Instance

    '''
    for response in responses:

        with open("COData_DouglasCounty.txt", 'a') as f:
            f.write(json.dumps(response))

        if len(response) < 15:
            print("Less than 15 Entries are present")
        else:
            db_collection.insert_many(response)

    print("Please check the current directory for the JSON formatted text file containing Data.\
        All the data in the files have been copied to MongoDB Instance")


if __name__ == '__main__':
    '''
    Queries data depending on the required parameters
    Uses basic authentication via Requests library

    '''

    API_Key = 'Use your API Key'
    API_Secret = 'Use your API Secret'
    basic = HTTPBasicAuth(API_Key, API_Secret)

    db_client_mongo = MongoClient("mongodb+srv://<usename>:<password>@codata.4ricoyc.mongodb.net/?retryWrites=true&w=majority")
    db = db_client_mongo.COData  # Creating a Database
    db_collection = db.douglas  # Creating a collection

    responses = list(getData())  # Calling function to fetch CO specific data from the API Endpoint
    dataWrite(db, db_collection, responses)  # Writes JSON data from getData() function to MongoDB
