#!/usr/bin/python3
VERSION = "v0.1"


"""
Next steps:
    Figure out connection to the MongoDb
        Using PyMongo (install using pip3)
    Create MongoQuery from the yes_list, no_list
    Sort query and print out
    Populate the mongo database
    test? Ha
"""

def main():
    yes_activities = []
    no_activities = []

    print("Welcome to Hubbub!", VERSION)


    print("Please enter some activities you are interested in!")
    while(True):
        a = input("Enter: ")
        if(a == ""):
            break
        yes_activities.append(a)


    print("Please enter some activities you are NOT interested in!")
    while(True):
        a = input("Enter: ")
        if(a == ""):
            break
        no_activities.append(a)

    print("Calculating the perfect fit... ")
    print(no_activities)


main()
