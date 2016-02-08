import commands
import database

def time_handler(time_passed):
    active_users = commands.get_active_users()
    if time_passed == 300:
        for user in active_users:
            database.post("points", "user", user, "points", points)

def initiator():
    all_users = commands.get_all_users()
    for user in all_users:
        database.post("points", "user", user, "points", 0)
