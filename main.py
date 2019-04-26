#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

VERSION = "v0.1"

activities_map = {}

def attemptMongoConnection():
    cred_file = open("credentials.txt","r")
    mongo_ip = cred_file.readline()
    connection_string = "mongodb://" + mongo_ip.strip()
    connection = MongoClient(connection_string)
    db = connection.hubbub
    activities = db.activities
    return activities


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

def temp_main():
    seed_activites_map()
    a = input("Enter a tag: ")
    doQuery(a)
    print_activities()



temp_main()


# def main():
#     activities = attemptMongoConnection()
#
#     print("Welcome to Hubbub!", VERSION)
#     people = input("How many people are participating? ");
#from bson.objectid import ObjectId

#     a = input("What is the time: [d]ay, [n]night >>> ")
#     if(a == 'n'):
#         doQuery(activities, "night")
#     else if(a == 'd'):
#         doQuery("day")
#     else:
#         print("Thats not valid!")


    #
    #
    #
    # print("Please enter some tags you are interested in!")
    # while(True):
    #     a = input("Enter: ")
    #     if(a == ""):
    #         break
    #     yes_tags.append(a)
    #
    # print("Please enter some activities you are NOT interested in!")
    # while(True):
    #     a = input("Etemp_main()
#nter: ")
    #     if(a == ""):
    # activities = attemptMongoConnection()
    #         break
    #     no_tags.append(a)
    #
    # print("Calculating the perfect fit... ")
    # print(no_tags)
