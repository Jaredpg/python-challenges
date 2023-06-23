try:
    # Open file in read-only mode
    with open("not_here.txt", 'r') as f:
        f.write("Hello World!")
except IOError as e:
    print("An error occurred:", e)