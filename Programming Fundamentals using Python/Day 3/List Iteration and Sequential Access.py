'''
Creating an empty list-
sample_list=[]	

Creating a list with known size and known elements-	
sample_list1=["Mark",5,"Jack",9, "Chan",5] sample_list2=["Mark","Jack", "Chan"]        #	List can store both homogeneous and heterogeneous elements

Creating a list with known size and unknown elements-
sample_list=[None]*5                        #	None denotes an unknown value in Python

Length of the list-
len(sample_list)	                                #Displays the number of elements in the list

Random access of elements:

Random read-
print(sample_list[2])	

Random write-
sample_list[2]=“James”	                #List is mutable i.e., the above statement will rewrite the existing value at index position 2 with “James”.

Other operations:

Adding an element to the end of the list-
sample_list.append("James")                     #	List need not have a fixed size, it can grow dynamically

Concatenating two lists-
new_list=["Henry","Tim"]

sample_list+=new_list
sample_list=sample_list+new_list	        #sample_list+=new_list, concatenates new_list to sample_list

sample_list=sample_list+new_list           # creates a new list named sample_list containing the concatenated elements from the original sample_list and new_list
'''
list_of_airlines=["AI","EM","BA"]

print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])

print("Iterating the list using keyword in")
for airline in list_of_airlines:
    print(airline)
    
    
