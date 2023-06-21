import os 
from tkinter import Y
from tracemalloc import stop

print("press anything to start: ")
x = input("")
#while x != 0:
print("this is my record management project: ")
print("1 - access records")
print("2 - create records")
print("3 - delete records")
#print("4 - other... ")
    

x = int(input(""))
if x == 1:
    print("you have chosen to access records: ")
    print("which records would you like to access")
    print("1 - birthday")
    print("2 - favourite food")
    print("3 - pets")
    #print(4 - to go back")
    y = int(input(""))

    if y == 1:
        print("accessing birthday records")
        birthday = open("birthday.txt", "r")
        print(birthday)

        #print("my birthday is on the 1st of January")
        #print("i was born in 2008")
        #print("my star sign is a capricorn")
    if y == 2:
        print("accessing favourite foods records")
        favfoods = open("favouritefoods.txt", "r")
        
        print(favfoods)

        #print("my favourite food is baked pretzels")
        #print("my favourite icecreams are chocolate, vanilla, cookies and cream, and ube")

    if y == 3:
        print("accessing pet records")
        pets = open("pets.txt", "r")
        pets.read()
        print(pets)

        #print("i have a dog")
        #print("his name is peanut")
        #print("he is 3 years old")
        #print("his dog breed is a pomeranian")

if x == 2:
    print("you have chosen to create records! ")
    print("write what you would like to save: ")
    create_record = input("")
    print("are you sure you would like to save " + create_record + "?")
    print("1 = yes, 2 = no")
    answer = int(input(""))
    if answer == 1:
        print(create_record + " has been saved into the library")
    if answer == 2:
        print(create_record + " has beem discarded")
    
if x == 3:
    print("you have chosen to delete information: ")
    print("what information would you like to delete? ")
    print("1 - birthday")
    print("2 - favourite food")
    print("3 - pets")

    delete_record = int(input(""))
    print("are you sure you would like to delete " + str(delete_record) +"?")
    print("1 = yes, 2 = no")
    answer = int(input)("")





