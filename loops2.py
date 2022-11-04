import random

colors=["red","blue","green","violet","brown","yellow","white","black","grey","orange"]

while True:
    color=colors[random.randint(0,len(colors)-1)]
    guess=input("I'm thinking about a color, can you guess it: ")

    while True:
            if (color==guess):
                break
            else:
                guess=input("Nope.Try again: ")

    print("You guessed it! I was thinking about", color)

    play_again=input("Let's play again? Type 'no' to quit.")

    if play_again.lower()=='no':
         break

print("It was fun, thanks for playing!")
