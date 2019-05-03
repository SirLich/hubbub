#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

VERSION = "v1.0"

activities_map = {}
TAGS = [
'day','night','outside','inside','summer','fall','spring','winter','active','relaxed','productive','recreational','remote','local'
]

DEV_MODE = False

def attemptMongoConnection():
    try:
        cred_file = open("credentials.txt","r")
        mongo_ip = cred_file.readline()
        connection_string = "mongodb://" + mongo_ip.strip()
        connection = MongoClient(connection_string)
        db = connection.hubbub
        activities = db.activities
        return activities
    except Exception as e:
        print("The Mongo connection failed!")

db = attemptMongoConnection()

def seed_activites_map():
    for a in db.find():
        activities_map[a["name"]] = 0

def do_query(tag, people):

    fil = {
    'tags': tag
    }

    # ,
    # 'min_people': {'$gte': people},
    # 'max_people': {'$lte' : people}

    for a in db.find(fil):
        activities_map[a["name"]] = activities_map[a["name"]] + 1

def dev_mode_print():
    s = [(k, activities_map[k]) for k in sorted(activities_map, key=activities_map.get, reverse=True)]
    for k, v in s:
        print(k,v)

def print_activities():
    out_list = []
    s = [(k, activities_map[k]) for k in sorted(activities_map, key=activities_map.get, reverse=True)]
    for k in s:
        out_list.append(k[0])

    print("")
    print("These activities were the best fit: ")
    for i in range(3):
        print(out_list[i])

    print("")
    print("You might also consider: ")
    for i in range(3,8):
        print(out_list[i])

def view_all():
    for a in db.find():
        print(a['name'])

def play():
    seed_activites_map()
    print("")

    people = int(input("Enter the number of people participating >>> "))
    print("")
    a = input("Is it: [d]ay or [n]ight, other input to skip >>> ")
    if(a == 'd'):
        do_query("day", people)
    elif(a == 'n'):
        do_query("night", people)
    else:
        print("Question skipped")
    print("")

    a = input("Is it: [sp]ring, [su]mmer, [f]all or [w]inter, other input to skip >>> ")
    if(a == 'sp'):
        do_query("spring", people)
    elif(a == 'su'):
        do_query("summer", people)
    elif(a == 'f'):
        do_query("fall", people)
    elif(a == 'w'):
        do_query("winter", people)
    else:
        print("Question skipped")
    print("")

    a = input("Do you want to hangout: [i]nside or [o]utside?, other input to skip >>> ")
    if(a == 'i'):
        do_query("inside", people)
    elif(a == 'o'):
        do_query("outside", people)
    else:
        print("Question skipped")
    print("")

    a = input("How are do you want to feel: [a]ctive or [r]elaxed?, other input to skip >>> ")
    if(a == 'a'):
        do_query("active", people)
    elif(a == 'r'):
        do_query("relaxed", people)
    else:
        print("Question skipped")
    print("")

    a = input("Can you travel: [l]ocal or [r]emote?, other input to skip >>> ")
    if(a == 'l'):

        do_query("local", people)
    elif(a == 'r'):
        do_query("remote", people)
    else:
        print("Question skipped")
    print("")

    a = input("Do you want your activity to be: [p]roductive or [r]ecreational?, other input to skip >>> ")
    if(a == 'p'):
        do_query("productive", people)
    elif(a == 'r'):
        do_query("recreational", people)
    else:
        print("Question skipped")
    print("")

    print("Calculating the perfect fit... ")
    print("")

    if(DEV_MODE):
        dev_mode_print()
    else:
        print_activities()
    activites_map = {}

def add_activity():
    try:
        print("")
        build_activity = {}
        build_activity['tags'] = []
        print("Answer the following questions about your activity to add it to the database")
        print("")
        build_activity['name'] = input("What is the activity called: ")
        build_activity['min'] = abs(int(input("Enter the min number of individuals required: ")))
        build_activity['max'] = abs(int(input("Enter the max number of individuals allowed: ")))
        print("")
        print("Available tags: ")
        for a in TAGS:
            print(a)
        print("")

        print("Enter tags you want to add: [a]ccept and continue, [q]uit and cancel")
        while(True):
            t = input("Tag: ")
            if(t == "a"):
                break
            if(t == 'q'):
                print("Successfully canceled")
                return
            if(t in TAGS and t not in build_activity['tags']):
                build_activity['tags'].append(t)
            else:
                print("Skipped. Either duplicate or invalid. Try again.")
        db.insert(build_activity)
        print("We have added your activity!")

    except Exception as e:
        print("Don't do that")

def delete_activity():
    view_all()
    print("")
    activity_name = input("Enter the activity you want to delete >>> ")
    fil = {
    'name': activity_name
    }

    db.remove(fil)
    print(activity_name, "has been deleted!")
def main():
    global DEV_MODE

    for i in range(150):
        print("")
    keep_playing = True
    print("")
    print("Welcome to Hubbub!", VERSION)
    print("")

    while(keep_playing):
        a = input("Pick an action: [p]lay, [v]iew all activities, [a]dd activity, [q]uit>>> ")

        if(a == 'p'):
            play()
        elif(a == 'v'):
            view_all()
        elif(a == 'a'):
            add_activity()
        elif(a == 'beans'):
            print("Cool beaaanzz bro")
        elif(a == 'q'):
            keep_playing = False
        elif(a == 'd'):
            DEV_MODE = not DEV_MODE
            print("Dev-mode is now:", DEV_MODE)
        elif(a == 'delete'):
            delete_activity()
        else:
            print("We couldn't proccess that query. Please try again.")
        print("")


    print("Goodbye!")

main()
