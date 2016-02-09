# http://ozgur.github.io/python-firebase/

# from firebase import firebase
import requests
import json

firebase_url = "https://iteksamen.firebaseio.com/"
# firebase = firebase.FirebaseApplication(firebase_url, None)

## todo: correct post function. Rewrite get function to work with members table and not just hvadsiger

def post(table, url, msg):
    msg_json = json.dumps(data)
    requests.post(firebase_url+table+url+".json", msg_json)


def get_unique_id(table, key_name, value_name):
    key_value = {}
    r = requests.get(firebase_url+table+".json")
    r = json.loads(r.text)
    for pair in r:
        key = r[pair][key_name]
        value = r[pair][value_name]
        key_value[key] = value
    return key_value


def get(url):
    table_data = requests.get(firebase_url+url+".json")
    table_data = json.loads(table_data.text)
    return table_data

def put(url, value):
    to_post = json.dumps(value)
    r = requests.put(firebase_url+url+".json", data=to_post)
