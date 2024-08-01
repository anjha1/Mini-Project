import requests

API_KEY = "3Krrph11i4fNx1CDd6U-sL_NPCvMP4lqB97d8xVYApk5"

def get_access_token():
    token_response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    )
    return token_response.json()["access_token"]

def score_data(array_of_values_to_be_scored):
    mltoken = get_access_token()
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    array_of_input_fields = ["day", "month", "year", "Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "DC", "ISI", "BUI", "Classes", "Region"]

    payload_scoring = {
        "input_data": [{
            "fields": array_of_input_fields,
            "values": array_of_values_to_be_scored
        }]
    }

    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/684ff05e-c3ae-40db-935f-92a8fda8c6b6/predictions?version=2021-05-01',
        json=payload_scoring,
        headers=header
    )
    return response_scoring.json()
