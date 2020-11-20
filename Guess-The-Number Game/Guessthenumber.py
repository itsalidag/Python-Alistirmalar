#Guess teh Number Game.

import random

a = random.randint(0,100)

print("""=====Welcome to Guess the Number Game.=====\n
      You Should guess the number ı think. But dont worry, \n
      ı'll be assisting you through process. Just give me a number.""")

def numberquiz(guess):
    guess = int(guess)
    if guess == a:
        print("You were Correct! coungratulations. ")
    elif guess > a:
        print("that was bigger than my number.")
    elif guess<a:
        print("that was smaller than my number")
    elif a > 10:
        print("game over.")
print(a)
b = 0 
while b < 10:
    guess = int(input("Guess the number: "))
    numberquiz(guess)
    if guess == a:
        b += 11
    else:    
        b +=1
    
