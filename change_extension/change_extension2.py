filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
splifiles = filenames.split(".")
for i in splifiles:
    if i[1] == "hpp":
        path = filename.rsplit( ".", 1 )[ 0 ]
        path += ".h"
        return path
    

print(splifiles) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]