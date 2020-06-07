#PF-Assgn-31
def check_palindrome(word):
    pass
    if word[::-1] == word:
        return 1
    else:
        return 0

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
    
    
#**********************************************************************************

#PF-Assgn-31
def check_palindrome(word):
    
    if word[0:]!=word[::-1]:
        return False
    return True

status=check_palindrome("civic")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
