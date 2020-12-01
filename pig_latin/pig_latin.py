def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split(" ")
  lia = []
  newmessage = ""
  for word in words:
    # Create the pig latin word and add it to the list
    kelword = word[1:]
    kelword += word[0]
    kelword += "ay"
    lia.append(kelword)
    # Turn the list back into a phrase
  for i in lia[:(len(lia))]:
      newmessage +=i
      newmessage += " "
      
  aslmsg = newmessage[:int(len(newmessage)-1)]
  return aslmsg,len(aslmsg)
         
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"