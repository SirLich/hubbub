#!/usr/bin/python3
VERSION = "v0.1"

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
