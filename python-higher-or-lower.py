import random
# from timeit import repeat
guess_number = random.randint(1, 100)
print("a random number has been generated")
x = int(input("guess the number generated betweeen 1-100: "))

while x != int(guess_number):
    if x > int(guess_number):
        print("your number was higher than the random number")
        x = int(input("guess again your number was higher: "))
    

    if x < int(guess_number):
        print("your number was lower than the random number")
        x = int(input("guess again your number was lower: "))
    
print("your answer is correct the number is " + str(guess_number))

