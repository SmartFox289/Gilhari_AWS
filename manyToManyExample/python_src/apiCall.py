import requests 
import json 

userUrl = 'http://localhost:80/gilhari/v1/user/'
projectUrl = 'http://localhost:80/gilhari/v1/project/'
collaborationUrl = 'http://localhost:80/gilhari/v1/collaboration/'


def getCall(url):
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


def postCall(url, dataDump):
    try: 
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, json = dataDump, headers = headers)

        if response.status_code == 201:
            print("Successfully inserted values")

        else:
            print(f"Error: {response.status_code}") 

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") 


getCall(userUrl)
getCall(projectUrl)
getCall(collaborationUrl)

with open('userData.json', 'r') as f:
    jsonData = json.load(f) 
postCall(userUrl, jsonData)

with open('projectData.json', 'r') as f:
    jsonData = json.load(f) 
postCall(projectUrl, jsonData)

with open('collaborationData.json', 'r') as f:
    jsonData = json.load(f) 
postCall(collaborationUrl, jsonData)

