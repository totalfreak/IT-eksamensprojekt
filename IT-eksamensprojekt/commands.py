# https://api.slack.com/methods

from slacker import Slacker
from slackclient import SlackClient
import requests
import database
import json
import random

token = "xoxb-20271825763-77FYy5JzaRFxmPliJ5Q5s5g1"

# dict of users and corresponding ID
users = {'aagaard': 'U0C5TCHEK',
        'michael': 'U0C5T6GSZ',
        'benjamin': 'U0C61DM5F',
        'frederik': 'U0C5TGLB1',
        'andreas': 'U0C5RJ97W',
         'johannes': 'U0C5THULX',
         'lyngsie': 'U0C64J674',
         'mik': 'U0CQSJ7RD',
         'mikkel': 'U0CT54KC4',
         'niklas': 'U0D67EX8A',
         'jacob': 'U0CNCAVB6',
         'philip': 'U0C5RGXB6',
         'simon': 'U0C5WNBRD',
         'joe': 'U0CQLHDPA',
         'daniel': 'U0C5RA3P0',
         'nazimod': 'U0C5VGK7A'}

users_id =  dict (zip(users.values(),users.keys())) # flips keys and values in the dict 'users'

slack = Slacker(token)

# slack utilities
def post_message(text):
    slack.chat.post_message("#random",text,"dank-bot",'','','','','','','',":dank:")

def get_active_users():
    r = requests.get('https://slack.com/api/users.list?token='+token+'&presence=1&pretty=1')
    r = json.loads(r.text)
    active_users = []
    for user in r['members']:
        if user['presence'] == 'active' and user['is_bot'] == 'False':
            active_users.append(user['profile']["real_name"])
    return active_user

def get_all_users():
    r = requests.get('https://slack.com/api/users.list?token='+token+'&presence=1&pretty=1')
    r = json.loads(r.text)
    all_users = []
    for user in r['members']:
        all_users.append(user['profile']["real_name"])
    return all_users

# !-triggered commands
def get_id(text,user):
    if text.split()[0] == 'id':
        post_message('@' + users_id[user] + ': Your ID is ' + user)

def get_toppost(text):
    if text.split()[0] == "toppost":
        subreddit = text.split()[1]
        json_raw=requests.get('https://www.reddit.com/r/' + subreddit + '/top/.json?sort=top&t=day/',
                              headers={"user-agent":"slackbot-schoolproject (By /u/MrAagaard)"}).text
        json_info = json.loads(json_raw)
        post_title = json_info['data']['children'][0]['data']['title']
        print "debugging"
        imgur_link = json_info['data']['children'][0]['data']['url']

        post_message("*Title*: " + post_title + " \n " + imgur_link + " \n " + "*From subreddit*: " + subreddit)

def hvad_siger(text):
    if text.split()[0] == "hvadsiger":
        img_dict = database.get('hvadsiger', 'img_url', 'img_type')
        randint = random.randint(0,1)
        y_or_n = ""
        img_bool = []
        for img in img_dict:
            if randint == 0 and img_dict[img] == "No":
                img_bool.append(img)
                y_or_n = "Nej :biblethump:"
            elif randint == 1 and img_dict[img] == "Yes":
                img_bool.append(img)
                y_or_n = "Ja :pogchamp:"
        img_url = img_bool[random.randint(0,len(img_bool)-1)]
        post_message(img_url + " *" + y_or_n + "!*")
