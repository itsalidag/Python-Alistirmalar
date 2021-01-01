import random 

hearts5 = ["♥♥♥♥♥","♥♥♥♥X","♥♥♥XX","♥♥XXX","♥XXXX"]
hearts10 = ["♥♥♥♥♥♥♥♥♥♥","♥♥♥♥♥♥♥♥♥","♥♥♥♥♥♥♥♥","♥♥♥♥♥♥♥","♥♥♥♥♥♥","♥♥♥♥♥","♥♥♥♥","♥♥♥","♥♥","♥","X","X"]
hearts5.reverse()
hearts10.reverse()
number = random.randint(1,100)
game = True
setting = ["e", "h"]
chose = input("select game setting: e (easy), h (hard)")
lives = 0
if chose =="e":
    lives = 10
elif chose == "h":
    lives = 5
while game:
    guess = int(input("make a guess: "))
    if guess == number:
        print("You Win!")
        game = False
        break
    elif number-3<guess<number+3:
        print("nearly finish!!!")
    elif number-10<guess<number+10:
        print("So Close!")
    elif number>guess:
        print("too low.")
    elif guess>number:
        print("too high")
    lives-=1 
    print("lives: ", lives)
       
    if lives ==0:
        print("out of lives. the answer was", number)
        game = False
    