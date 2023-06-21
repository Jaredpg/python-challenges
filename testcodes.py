def main():
    sentence = input("Please enter sentence(s): ")
    num_words = len(sentence.split(' '))

    counter = 0
    for x in sentence:
        if x in "!?.":
            counter += 1

    print("There are", counter, "sentences and", num_words, "words.")

while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break

import os

# list files from a working directory
print(os.listdir())

# verify file exist
print(os.path.isfile('sales.txt'))