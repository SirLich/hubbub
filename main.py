#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint

VERSION = "v0.1"

def attemptMongoConnection():
    cred_file = open("credentials.txt","r")
    mongo_ip = cred_file.readline()
    connection_string = "mongodb://" + mongo_ip.strip() + "/hubbub"
    db = MongoClient(connection_string)
    collection = db["activities"]
    return collection



"""
Next steps:
    Figure out connection to the MongoDb
        Using PyMongo (install using pip3)
        pip3 install --user pymongo

    Create MongoQuery from the yes_list, no_list
    Sort query and print out
    Populate the mongo database
    test? Ha
"""

def main():
    yes_tags = []
    no_tags = []

    connection = attemptMongoConnection()

    print("Welcome to Hubbub!", VERSION)
    people = input("How many people are participating? ");
    print("Please enter some tags you are interested in!")
    while(True):
        a = input("Enter: ")
        if(a == ""):
            break
        yes_tags.append(a)

    print("Please enter some activities you are NOT interested in!")
    while(True):
        a = input("Enter: ")
        if(a == ""):
            break
        no_tags.append(a)

    print("Calculating the perfect fit... ")
    print(no_tags)

main()
