import requests 
import json 

get_url = 'http://localhost:80/gilhari/v1/Employee/'
post_url = 'http://localhost:80/gilhari/v1/Employee/'


def get_call(url):
    try: 
        response = requests.get(url)

        if response.status_code == 200:
            print("Successfuly called GET API")
            print("GET Response data: ")
            print(response.json()) 

        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") 


def post_call(url, dataDump):
    try: 
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, json = dataDump, headers = headers)

        if response.status_code == 201:
            print("Successfully inserted values")

        else:
            print(f"Error: {response.status_code}") 

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") 


get_call(get_url)

with open('emp_data_transformed.json', 'r') as f:
    json_data = json.load(f) 

post_call(post_url, json_data)
