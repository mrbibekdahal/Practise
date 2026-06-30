import random

secret_numb = random.randint(1,100)
attempts = 0
while True:
    num =  int(input("Enter a number: "))
    attempts +=1

    if num> secret_numb:
        print("Too High")

    elif num < secret_numb:
        print("too low")
    
    else:
        print("You got it") 

        print("Congratulations !!!!!\nYou guessed correct in just", attempts,"attempt(s)\n")
        break