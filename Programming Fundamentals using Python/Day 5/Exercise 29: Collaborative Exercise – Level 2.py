#PF-Exer-29
def merge_lists(list1,list2):
    new_merge_list = list1 + list2 
    return new_merge_list
    
def sort_list(merged_list):
    merged_list.sort() 
    return merged_list

#Provide different values for list1 and list2 and test your program
merged_list=merge_lists(list1=[1,2,3,4,1] ,list2=[2,3,4,5,4,6])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)

'''
[1, 2, 3, 4, 1, 2, 3, 4, 5, 4, 6]
[1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 6]
'''
