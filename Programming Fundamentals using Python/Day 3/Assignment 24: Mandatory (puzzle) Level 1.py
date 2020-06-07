#PF-Assgn-24
def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if((num1+num2)<=num3 or (num2+num3)<=num1 or (num3+num1)<=num2):
        print(failure)
    else:
        print(success)

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)
