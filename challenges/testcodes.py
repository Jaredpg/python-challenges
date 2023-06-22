import os

# Absolute path of a file
old_name = ("project-records/" + input(""))
new_name = ("project-records/" + input(""))

# Renaming the file
os.rename(old_name, new_name)