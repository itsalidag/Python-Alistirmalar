filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

for i in filenames:
    a = i.split(".")
    newfilenames = []
    if a[1] == "hpp":
        newext = "h"
        a.pop(1)
        a.append(newext)
        newfilename = a[0] + "." + a[1]
        newfilenames.append(newfilename)
    else:
        newfilenames.append(i)
        
    newfilenameza = [str(i) for i in newfilenames]
    
    print(newfilenameza)

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]