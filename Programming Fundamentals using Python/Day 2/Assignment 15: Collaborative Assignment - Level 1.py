#PF-Assgn-15

def find_product(num1,num2,num3):
    message=0
    if(num1%7==0):
        message=num2*num3
    elif(num2 %7 == 0):
        message=num3
    elif(num3 %7 == 0):
        message=-1
    else:
        message=num1*num2*num3
    return message
#(int) (input(“Enter a number:”))

#Provide different values for num1, num2, num3 and test your program
message=find_product(7,6,2)
print(message)
