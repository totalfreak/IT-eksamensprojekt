import commands
import database


def give_active_users_points():
    active_users = commands.get_active_users()
    points_dict = get_points()
    for user_id in active_users:
        points_dict[commands.users_id[user_id]] += 10
        name = commands.users_id[user_id]
        user_point = points_dict[name]
        print name, "has", user_point, "points"
        database.put("members/"+name+"/points", user_point)

def get_points(): # Returns a dictionary of user each users name and their number of points e.g. {'aagaard': 42, 'benjamin', 2 ...}
    members = database.get('members','')
    points_dict = {}
    for user in members:
        points_dict.update({user: members[user]['points']})
    return points_dict

# Example of adding a new row
# >>> for name in commands.users:
# ...     requests.put('https://iteksamen.firebaseio.com/members/'+name+'/messages_sent.json','0')
