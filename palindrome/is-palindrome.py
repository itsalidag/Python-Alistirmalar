

def is_palindrome(string):
    slt = string.split(" ")
    newmsg = ""
    
    for i in slt:
        for a in i:
            newmsg += a
    newmsg = newmsg.lower()
    reversedd = newmsg[::-1]        
    
    if reversedd == newmsg:
        return True
    else:
        return False
    


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True