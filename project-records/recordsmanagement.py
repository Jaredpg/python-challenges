
import os
from tracemalloc import start 
from openpyxl import Workbook
print("press anything to start: ")
records_start = input("")

while records_start:
    print("this is my record management project: ")
    print("1 - access records")
    print("2 - create records")
    print("3 - delete records")
    print("4 - exit program")
    
    records_start = int(input(""))

    
    if records_start == 1:
        print("you have chosen to access records: ")
        print("1 - pre-defined records")
        print("2 - saved records")
        print("3 - cancel action")
        access_record = int(input(""))

        if access_record == 1:
            print("which records would you like to access")
            print("1 - birthday")
            print("2 - favourite food")
            print("3 - pets")
            print("4 - cancel action")

            record_option = int(input(""))

            if record_option == 1:
                print("accessing birthday records")
                birthday = open("project-records/birthday.txt", "r")
                print(birthday.read())
                print("")
                answer = int(input("press 1 to go back or 2 to exit: "))
                if answer == 1:
                    print("you have chosen to go back ")
                    print("")
                    records_start = True
                elif answer == 2:
                    print("program exited")
                    break   

            elif record_option == 2:
                print("accessing favourite foods records")
                favfoods = open("project-records/favouritefoods.txt", "r")
                print(favfoods.read())
                print("")
                answer = int(input("press 1 to go back or 2 to exit: "))
                if answer == 1:
                    print("you have chosen to go back ")
                    print("")
                    records_start = True
                elif answer == 2:
                    print("program exited")
                    break

            elif record_option == 3:
                print("accessing pet records")
                pets = open("project-records/pets.txt", "r")
                print(pets.read())
                print("")
                answer = int(input("press 1 to go back or 2 to exit: "))
                if answer == 1:
                    print("you have chosen to go back ")
                    print("")
                    records_start = True
                elif answer == 2:
                    print("")
                    print("program exited")
                    break

            elif record_option == 4:
                print("action cancelled")
                print("")
                answer = int(input("press 1 to go back or 2 to exit: "))
                if answer == 1:
                    print("you have chosen to go back ")
                    print("")
                    records_start = True
                elif answer == 2:
                    print("program exited")
                    break

        elif access_record == 2:
            print("accessing saved records...")
            print("")
            print("saved records not found")
            print("")
            answer = int(input("press 1 to go back or 2 to exit: "))
            if answer == 1:
                print("you have chosen to go back ")
                print("")
                records_start = True
            elif answer == 2:
                print("program exited")
                break
            #unfinished
            
        elif access_record == 3:
            print("action cancelled")
            print("")
            answer = int(input("press 1 to go back or 2 to exit: "))
            if answer == 1:
                print("you have chosen to go back ")
                print("")
                records_start = True
            elif answer == 2:
                print("program exited")
                break


    elif records_start == 2:
        print("you have chosen to create records! ")
        print("1 - create a new file")
        print("2 - input user data to excel")
        print("3 - cancel create")

        reply = int(input(""))
        if reply == 1:
            print("write what you would like to save: ")

            file_name = "project-records/" + input('Filename with extension, e.g. example.txt: ')

            with open(file_name, 'w', encoding='utf-8') as my_file:
                my_file.write(input('Your message: '))

            print("file has been saved into library")
            print("")
            answer = int(input("press 1 to go back or 2 to exit: "))
            if answer == 1:
                print("you have chosen to go back ")
                print("")
                records_start = True
            elif answer == 2:
                print("program exited")
                break

        elif reply == 2:
            name = input("write down your full name: ")
            birthday = input("write down your birthday: ")
            favcolour = input("write down your favourite colour: ")
            print("data has been save")
            print("")
            print("name: " + name)
            print("birthday: " + birthday)
            print("fovourite colour: " + favcolour)

            wb = Workbook()
            ws = wb.active
            ws['A1'] = "name"
            ws['B1'] = "birthday"
            ws['C1'] = "favourite colour"
            ws.append([name, birthday, favcolour])
            user_filename = input("insert file name: ")
            wb.save("project-records/" + user_filename + ".xlsx")
        
        elif reply == 3:
            print("creation cancelled")

    elif records_start == 3:
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

            delete_option = int(input(""))
            if delete_option == 1:
                print("record is unable to be deleted")
                print("")
                answer = int(input("press 1 to go back or 2 to exit: "))
                if answer == 1:
                    print("you have chosen to go back ")
                    print("")
                    records_start = True
                elif answer == 2:
                    print("program exited")
                    break
                
            elif delete_option == 2:
                print("deletion has been cancelled")
                print("")
                answer = int(input("press 1 to go back or 2 to exit: "))
                if answer == 1:
                    print("you have chosen to go back ")
                    print("")
                    records_start = True
                elif answer == 2:
                    print("program exited")
                    break

        elif delete_record == 2: 
            print("are you sure you would like to delete this file?")
            print("1 = yes, 2 = no")
            answer = int(input(""))
            if answer == 1:
                print("record is unable to be deleted")
            elif answer == 2:
                print("deletion has been cancelled")
    

        elif delete_record == 3: 
            print("are you sure you would like to delete this file?")
            print("1 = yes, 2 = no")
            answer = int(input(""))
            if answer == 1:
                print("record is unable to be deleted")
            elif answer == 2:
                print("deletion has been cancelled")
            
        elif delete_record == 4:
            input_delete_record = input("input the file you would like to delete: ")
            print("looking for file...")
            deletion = os.remove("project-records/" + input_delete_record)
            print("file has been deleted")
            print("")
            answer = int(input("press 1 to go back or 2 to exit: "))
            if answer == 1:
                print("you have chosen to go back ")
                print("")
                records_start = True
            elif answer == 2:
                print("program exited")
                break

        elif delete_record == 5:
            print("deletion cancelled")
            print("")
            answer = int(input("press 1 to go back or 2 to exit: "))
            if answer == 1:
                print("you have chosen to go back ")
                print("")
                records_start = True
            elif answer == 2:
                print("program exited")
                break

    elif records_start == 4:
        print("program has been exited")
        break
        