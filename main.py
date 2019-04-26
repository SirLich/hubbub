#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

VERSION = "v0.1"

activities_map = {}

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

def doQuery(tag):
    fil = {
    'tags': tag
    }

    for a in db.find(fil):
        activities_map[a["name"]] = activities_map[a["name"]] + 1

def print_activities():
    for a in activities_map:
        print(str(activities_map[a]), a)

def main():
    seed_activites_map()
    print("Welcome to Hubbub!", VERSION)
    print("")

    # people = input("How many people are participating? ");
    # print("")

    a = input("Is it: [d]ay or [n]ight, other input to skip >>> ")
    if(a == 'd'):
        doQuery("day")
    elif(a == 'n'):
        doQuery("night")
    else:
        print("Question skipped")
    print("")

    a = input("Do you want to hangout: [i]nside or [o]utside?, other input to skip >>> ")
    if(a == 'i'):
        doQuery("inside")
    elif(a == 'o'):
        doQuery("outside")
    else:
        print("Question skipped")
    print("")

    a = input("How are do you want to feel: [a]ctive or [r]elaxed?, other input to skip >>> ")
    if(a == 'a'):
        doQuery("active")
    elif(a == 'r'):
        doQuery("relaxed")
    else:
        print("Question skipped")
    print("")

    a = input("Can you travel: [l]ocal or [r]emote?, other input to skip >>> ")
    if(a == 'l'):
        doQuery("local")
    elif(a == 'r'):
        doQuery("remote")
    else:
        print("Question skipped")
    print("")

    a = input("Do you want your activity to be: [p]roductive or [r]ecreational?, other input to skip >>> ")
    if(a == 'p'):
        doQuery("productive")
    elif(a == 'r'):
        doQuery("recreational")
    else:
        print("Question skipped")
    print("")

    print("Calculating the perfect fit... ")
    print("")

    print_activities()

main()
