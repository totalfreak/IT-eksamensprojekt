from slackclient import SlackClient
import requests
import time
import json
import sched

import commands
import points

DEBUG = True

# found at https://api.slack.com/#auth
token = "xoxb-20271825763-77FYy5JzaRFxmPliJ5Q5s5g1"

# dict of users and corresponding ID
users = commands.users

# flips keys and values in the dict 'users'
users_id = dict(zip(users.values(), users.keys()))

sc = SlackClient(token)

current_time = {}
current_time['points'] = int(round(time.time()))

if sc.rtm_connect():  # if the connection is succesful start an infinite loop, which reads the data from the real time messaging api
    while True:
        data = sc.rtm_read() # reads data through slack's real time api and stores it in variable
        for action in data:  # action is now an array of information bound to different types of events. All events can be found here https://api.slack.com/events
            if action['type'] == 'message':  # start of message checking
                try:  # tries to find something to execute
                    text = action['text'].lower()
                    if text[0] == "!":
                        text = text[1:] # removes the "!" from any command which will be executed
                        commands.post_id(text, action['user'])
                        commands.post_toppost(text)
                        commands.post_hvadsiger(text)
                        commands.points_post(text, action['user'])
                        commands.points_roulette(text, action['user'])

                except Exception, e:  # catches errors and prints them out
                    print "Exception: " + e.message
            if DEBUG:
                print data
            time.sleep(1)
        if (int(round(time.time())) - current_time['points']) > 300:
            points.give_active_users_points()
            current_time['points'] = int(round(time.time()))
else:
    print "Connection Failed, invalid token?"
