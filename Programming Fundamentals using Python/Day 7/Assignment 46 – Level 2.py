#PF-Assgn-46
#Using Recursion:
def nearest_palindrome(number):
    number=number+1
    s=str(number)
    if s == s[::-1]:
        return number
    else:
        return nearest_palindrome(number)

number=12300
'''
99 is also a palindrome, but as per the problem,
the program should return a "Nearest" and "GREATER"
palindrome number than the given number.
'''
print(nearest_palindrome(number))

#************************************************************************************************

#PF-Assgn-46

def nearest_palindrome(number):
    number=number+1
    s=str(number)
    while(s!=s[::-1]):
        number=number+1
        s=str(number)
    return number

number=12300
print(nearest_palindrome(number))

# 12321
