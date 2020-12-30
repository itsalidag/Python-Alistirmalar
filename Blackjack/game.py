import random 

cards = ["A", 2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
base_cards =[]

game= True
ucard1= random.choice(cards)
ucard2 = random.choice(cards)
bcard1 = random.choice(cards)
bcard2 = random.choice(cards)
user_cards.append(ucard1)
user_cards.append(ucard2)
base_cards.append(bcard1)
base_cards.append(bcard2)
print("Your cards : ", user_cards)
print("base cards: ", base_cards[0])

base_total = 0
for i in base_cards:
    if i == "A":
        base_total+=11
    else:
        base_total+=i

b = 0
for i in user_cards:
    if i == "A":
        b +=11
    else:
        b+=i
print("user total is: ", b)
print("game total is : ", base_total)
while game:
    a = input("wanna play? ")
    if a == "y":
        new_num = random.choice(cards)
        user_cards.append(new_num)
        print(user_cards)
        b+=new_num
        print("new user total is :", b)
        if b > 21:
            print("you lose.")
            game = False
            break
    if a == "n":
        bnum = random.choice(cards)
        base_cards.append(bnum)
        print("my nums are: ", base_cards)
        print("base total is: ", base_total)
        print("game is now over. ")
        
        
        if b > base_total:
            print("user = ", b, "-"*10, "Pc = ", base_total)
            print("/"*15, "You Win!", "/"*15)
            game = False
        elif base_total>b:
            print("user = ", b, "-"*10, "Pc = ", base_total)
            print("/"*15, "Pc Wins", "/"*15)
            game = False
        else:
            print("an error occured.")
            game = False
            break