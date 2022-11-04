import random
number=random.randint(0,10)

guess=int(input("I am thinking about a number between zero and ten. Can you guess it? "))

while True:
    if guess == number:
        print("Correct!")
        break 
    else:
        guess=int(input("Nope.Try again: "))
        
