def remove_duplicates(value):
    #start writing your code here
    str=""
    for i in value:
        if i not in str:
            str=str+i
    return str

print(remove_duplicates("11223445566666ababzzz@@@123##"))


'''
123456abz@#

'''
