import random
guess_number = random.randint(1, 100)

x = int(input("guess the number generated betweeen 1-100: "))
if x == int(guess_number):
    print("your answer is correct the number is" + guess_number)

elif x >= guess_number:
    print("your guess a bit higher than the random number")
    

elif x <= guess_number:
    print("your guess is a bit lower than the random number")
    
while x >= guess_number:
    print("your guess a bit higher than the random number")
    x = int(input("guess the number generated betweeen 1-100: "))
    if x == int(guess_number):
        print("your answer is correct the number is" + guess_number)

while x <= guess_number:
    print("your guess is a bit lower than the random number")
    x = int(input("guess the number generated betweeen 1-100: "))
    if x == int(guess_number):
        print("your answer is correct the number is" + guess_number)


