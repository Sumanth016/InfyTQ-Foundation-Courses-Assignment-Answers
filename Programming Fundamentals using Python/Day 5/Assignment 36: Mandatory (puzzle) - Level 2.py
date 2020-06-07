#PF-Assgn-36
def create_largest_number(number_list):
    number_list.sort(reverse = True)
    new_number_list=[]
    for index,value in enumerate(number_list):
        ele=number_list.pop(index)
        number_list.insert(index,str(ele))
    return int("".join(number_list))
'''
The InfyTQ compiler also checks for data type.
After using the join function, it returns a string.
However, the required is datatype must be int.
Hence we convert it to int using the int()
'''
number_list=[23,45,67]
#number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)
