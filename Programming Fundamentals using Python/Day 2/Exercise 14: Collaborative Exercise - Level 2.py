def display(num):
    if(num>=80 and num<=100):
        message="A"
    elif(num>=73 and num<=79):
        message="B"
    elif(num>=65 and num<=72):
        message="C"
    elif(num>=0 and num<=64):
        message="D"
    else:
        message="Z"
    return message

#Provide different values for num and test your program
message=display(79)
print(message)
