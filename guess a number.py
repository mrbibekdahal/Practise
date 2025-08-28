

import random 
number = random.randint(0,100)
print("guess between 0 and 100")

guess = int(input("enter the number:"))

if guess == number:
    print("your guess is correct!!!")
elif guess > number:
    print("too high!!!")
elif guess < number:
    print("too low!!!")
