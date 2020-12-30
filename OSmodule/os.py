import os
print(os.name) #os name
print(os.path) # os path
print(os.getcwd()) #current working directory

try:
    filename = "trynot.txt" # -> specify the path for the file
    f = open(filename, "r") # -> open the file with os open command
    text = f.read() # -> read the file with read() command from os
    print(text) # -> now, the readed variable has saved to text
    f.close() # -> it is best to close file after we done with 
except IOError: # -> if we give unexpected path to the open method, it will crash with IO error.
    print("problem while opening", filename) # -> this will happen in case of any IO error.

# popen is same with open but with the pipe. Which makes the progress much easier. 

#os.rename("try.txt", "ali.txt") # to change name or extention of a file. 

os.path.join("tryingfolder")
print(os.getcwd())
os.dir()