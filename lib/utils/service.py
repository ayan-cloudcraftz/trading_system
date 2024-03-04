import requests
import urllib3
import json
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get(url:str):
    response = requests.get(url=url, verify=False)
    # response = requests.get(url=url)
    # print(response)
    # return response.text
    try:
        response_json = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print("got here")
        time.sleep(3)
        response = requests.get(url=url)
        response_json = json.loads(response.text)


    # print(response_json)
    return response_json
    

def post(url:str, body:dict):
    response = requests.post(url=url, verify=False, json=body)
    response_json = json.loads(response.text)
    # print(response_json)
    return response_json
    