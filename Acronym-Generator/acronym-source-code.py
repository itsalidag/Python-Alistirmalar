#acronym game.
#this program takes an user input and returns the best acronym for spesific string.

userInput = str(input("Name for Acronym: "))
splitted = userInput.split(" ")

def longword(splitted):
    firstletters = []
    acronyml = ""
    for i in splitted:
        firstletters.append(i[0])
    for i in firstletters:
        i = i.upper()
        acronyml += str(i)
    print("Best Acronym for {input}, Selected as {acronym}".format(input= userInput, acronym = acronyml))
    

def oneword(splitted):
    firstletters = []
    acronymo = ""
    for i in userInput:
        if i in ("b","c","ç","d","f","g","ğ","h","j","k","l","m","n","p","r","s","ş","t","v","y","z"):
            acronymo += str(i.upper())
    print("Best Acronym for {input}, Selected as {acronym}".format(input= userInput, acronym = acronymo))

if len(splitted) >1:
    longword(splitted)
else:
    oneword(splitted)