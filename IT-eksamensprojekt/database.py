# http://ozgur.github.io/python-firebase/

from firebase import firebase

firebase = firebase.FirebaseApplication('https://iteksamen.firebaseio.com/',None)

def post(database, key_name ,key, value_name, value):
     firebase.post('/'+database, {key_name: key, value_name: value})

def get(database, key_name, value_name):
    key_value = {}
    r = firebase.get('/'+database, None)

    for pair in r:
        key = r[pair][key_name]
        value = r[pair][value_name]
        key_value[key] = value
    return key_value
