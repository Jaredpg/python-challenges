import os

# Get the list of all files and directories
# in the root directory
path = "/"
#dir_list = os.listdir(path)

#print("project-records'", path, "' :")
#print(dir_list)
# print the list

file_list = os.listdir(path)
print(file_list)

import time
def animate(text):
    for i in range(len(text)):
        print(text[:i+1])
        time.sleep(0.1)


print("loading") 
animate("...")
