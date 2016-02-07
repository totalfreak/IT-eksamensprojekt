from slackclient import SlackClient
import requests
import time
import json

import commands

DEBUG = False

# found at https://api.slack.com/#auth
token = "xoxb-20271825763-77FYy5JzaRFxmPliJ5Q5s5g1"

# dict of users and corresponding ID
users = {'aagaard': 'U0C5TCHEK', 'michael': 'U0C5T6GSZ', 'benjamin': 'U0C61DM5F','frederik': 'U0C5TGLB1', 'andreas': 'U0C5RJ97W',
         'johannes': 'U0C5THULX', 'lyngsie': 'U0C64J674', 'mik': 'U0CQSJ7RD', 'mikkel': 'U0CT54KC4', 'niklas': 'U0D67EX8A',
         'jacob': 'U0CNCAVB6', 'philip': 'U0C5RGXB6', 'simon': 'U0C5WNBRD', 'joe': 'U0CQLHDPA', 'daniel': 'U0C5RA3P0', 'nazimod': 'U0C5VGK7A'}

# flips keys and values in the dict 'users'
users_id =  dict (zip(users.values(),users.keys()))


sc = SlackClient(token)
# if the connection is succesful start an infinite loop, which reads the data from the real time messaging api
if sc.rtm_connect():
    while True:

        data = sc.rtm_read() # reads data through slack's real time api and stores it in variable data
        for action in data: # action is now an array of information bound to different types of events. All events can be found here https://api.slack.com/events
            if action['type']  == 'message': # start of message checking
                try: # tries to find something to execute
                    text = action['text'].lower()
                    if text[0] == "!":
                        text = text[1:]
                        commands.get_id(text, action['user'])
                        commands.get_toppost(text)
                        commands.hvad_siger(text)

                # catches errors and prints them out
                except Exception, e:
                    print "Exception: " + e.message

            if DEBUG:
                print data
            time.sleep(1)
else:
    print "Connection Failed, invalid token?"
