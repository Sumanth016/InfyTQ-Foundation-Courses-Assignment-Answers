'''
ZeroDivisionError	- When a value is divided by zero	
num_list=[]
total=0
avg=total/len(num_list)

TypeError	- When we try to do an operation with incompatible data types	
total=10
total+="20"

NameError -	When we try to access a variable which is not defined	
avg=total/10 where total is not defined

IndexError -	When we try to access an index value which is out of range	
num_list=[1,2,3,4]
value=num_list[4]

ValueError -	When we use a valid data type for an argument of a built-in function but passes an invalid value for it	
#string is a valid data type for int() but the value “A” is invalid, as "A" can't be converted into int.
value="A"
num=int(value)
'''
#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print(total)
    except:
        print("Some error occured")
    print("Returning back from function.")

list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
