//PF-Exer-16
# Python Program to find the L.C.M. of two input number
def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm


num1=5
num2=10
print(compute_lcm(num1, num2))
//Write your code here
