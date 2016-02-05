# http://ozgur.github.io/python-firebase/

from firebase import firebase

firebase = firebase.FirebaseApplication('https://iteksamen.firebaseio.com/',None)

def post_response(trigger, response):
     firebase.post('/responses', {'trigger': trigger, 'response': response})
