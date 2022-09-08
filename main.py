import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    '''

    Queries data depending on the required parameters
    Uses basic authentication via Requests library

    '''

    API_Key = 'Enter your API Key'
    API_Secret = 'Enter your API Secret'
    basic = HTTPBasicAuth(API_Key, API_Secret)

    # Creating parameters for queries

    payload_leisure = {'area': '35', 'pertypdesc': 'Annual', 'indcode': '1026', '$limit': '30000'}
    payload_realEstate = {'area': '35', 'pertypdesc': 'Annual', 'indcode': '531', '$limit': '30000'}
    payload_information = {'area': '35', 'pertypdesc': 'Annual', 'indcode': '51', '$limit': '30000'}

    # Querying responses as per the parameters
    # Queries Douglas County, Annual, Informaiton/ Leisure and Hospitality/ Real Estate Informaiton

    response_leisure = requests.get("https://data.colorado.gov/resource/cjkq-q9ih.json", auth=basic, params=payload_leisure)
    response_realEstate = requests.get("https://data.colorado.gov/resource/cjkq-q9ih.json", auth=basic, params=payload_realEstate)
    response_information = requests.get("https://data.colorado.gov/resource/cjkq-q9ih.json", auth=basic, params=payload_information)

    # Writes to three different files based on the Industry/Code

    with open("CODataLeisure.txt", 'w') as f:
        f.write(json.dumps(response_leisure.json(), indent=2))

    with open("CODataRealEstate.txt", 'w') as f:
        f.write(json.dumps(response_realEstate.json(), indent=2))

    with open("CODataInformation.txt", 'w') as f:
        f.write(json.dumps(response_information.json(), indent=2))

    print("Please check the current directory for the JSON formatted text files")
