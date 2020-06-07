#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count=0
    for index,num in enumerate(num_list):
        for i in range(index+1,len(num_list)):
            if num+num_list[i]==n:
                count=count+1
    return count
    
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))

#*******************************************************************************************

#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count=0
    for i in range(len(num_list)):
        for j in range(i,len(num_list)):
            if(j<0 and i<0):
                continue
            if(num_list[i]==num_list[j]):
                continue
            if(num_list[i]+num_list[j]==n):
                count+=1
    if(count==0):
        return 0
    return count
#Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
