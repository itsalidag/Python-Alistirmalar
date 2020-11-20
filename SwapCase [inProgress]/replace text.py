#write a codde that takes an imput and returns it reversed, upper characterrs to low and low to up 

def reverse(sentence):
    mylist = []
    splitted = sentence.split(" ")
    for i in range(len(splitted)):
        mylist.append(splitted[-1])
        splitted.pop(-1)
        
    for i in mylist:
        chars = []
        for char in i:
            char = char.swapcase()
            chars.append(char)
            # if char.islower():
            #     char = char.upper()
            #     chars.append(char)
            # elif char.isupper():
            #     char = char.lower()
            #     chars.append(char)
            # else:
            #     char = char
            #     chars.append(char)
        print(chars)
        newmessage = ""
        for i in chars:
            newmessage += str(i)
        print(newmessage)
    #başarı ile işlemi tamamladık şimdi mesajı tekrar yazdıralım

reverse("helLo WorldeS")
