import os 

print("press anything to start: ")
x = input("")

print("this is my record management project: ")
print("1 - access records")
print("2 - create records")
print("3 - delete records")
print("4 - exit program")

x = int(input(""))
if x == 1:
    print("you have chosen to access records: ")
    print("which records would you like to access")
    print("1 - birthday")
    print("2 - favourite food")
    print("3 - pets")
    print("4 - cancel action")
    y = int(input(""))

    if y == 1:
        print("accessing birthday records")
        birthday = open("birthday.txt", "r")
        print(birthday.read())
        #answer = int(input("press 1 to go back or 2 to exit: "))
        #if answer == 1:
            #print("you have chosen to go back ")
        #if answer == 2:
            #print("program exited")

    if y == 2:
        print("accessing favourite foods records")
        favfoods = open("favouritefoods.txt", "r")
        print(favfoods.read())
        #answer = int(input("press 1 to go back or 2 to exit: "))
        #if answer == 1:
            #print("you have chosen to go back: ")
        #if answer == 2:
            #print("program exited")

    if y == 3:
        print("accessing pet records")
        pets = open("pets.txt", "r")
        print(pets.read())
        answer = int(input("press 1 to go back or 2 to exit: "))
        if answer == 1:
            print("you have chosen to go back: ")
        if answer == 2:
            print("program exited")

    if y == 4:
        print("action cancelled")
if x == 2:
    print("you have chosen to create records! ")
    print("1 - create a new file")
    print("2 - input profile data")
    print("3 - cancel create")

    reply = int(input(""))
    if reply == 1:
        print("write what you would like to save: ")

        file_name = 'example.txt'

        with open(file_name, 'w', encoding='utf-8') as my_file:
            my_file.write(input('write down your message: '))

        file_name = input('Filename with extension, e.g. example.txt: ')

        with open(file_name, 'w', encoding='utf-8') as my_file:
            my_file.write(input('Your message: '))

        print("file has been saved into library")

    if reply == 2:
        name = input("write down your full name: ")
        birthday = input("write down your birthday: ")
        favcolour = input("write down your favourite colour: ")
        print("data has been save")

        print("name: " + name)
        print("birthday: " + birthday)

        #answer = int(input("press 1 to go back or 2 to exit: "))
        #if answer == 1:
         #print("you have chosen to go back: ")
    
        #if answer == 2:
            #print("program exited")

    if reply == 3:
        print("creation cancelled")

if x == 3:
    print("you have chosen to delete records: ")
    print("what record would you like to delete? ")
    print("1 - birthday")
    print("2 - favourite food")
    print("3 - pets")
    print("4 - enter file")
    print("5 - cancel deletion")

    delete_record = int(input(""))

    if delete_record == 1: 
        print("are you sure you would like to delete this file?")
        print("1 = yes, 2 = no")

        answer = int(input(""))
        if answer == 1:
            print("your record has been deleted")
        if answer == 2:
            print("deletion has been cancelled")

    if delete_record == 2: 
        print("are you sure you would like to delete this file?")
        print("1 = yes, 2 = no")

        answer = int(input(""))
        if answer == 1:
            print("your record has been deleted")
        if answer == 2:
            print("deletion has been cancelled")

    if delete_record == 3: 
        print("are you sure you would like to delete this file?")
        print("1 = yes, 2 = no")

        answer = int(input(""))
        if answer == 1:
            print("your record has been deleted")
        if answer == 2:
            print("deletion has been cancelled")

    if delete_record == 4:
        input_delete_record = input("input the file you would like to delete: ")
        print("looking for file...")
        deletion = os.remove(input_delete_record)
        print("file has been deleted")

    if delete_record == 5:
        print("deletion cancelled")

if x == 4:
    print("program has been exited")





