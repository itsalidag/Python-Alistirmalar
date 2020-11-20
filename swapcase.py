
def reverse(sentence):
    mylist = []
    splitted = sentence.split(" ")
    for i in range(len(splitted)):
        mylist.append(splitted[-1])
        splitted.pop(-1)
    newmessage = ""
    for i in mylist:
        if i == " ":
            i = " "
        else:
            i = i.swapcase()
            newmessage += str(i)
    print(newmessage)
        
reverse("eben nasıl")

