'''
A dictionaries can be used to store an unordered collection of key-value pairs. The key should be unique and can be of any data type. Like lists, dictionaries are mutable.

Creating a dictionary-
crew_details={ "Pilot":"Kumar","Co-pilot":"Raghav","Head-Strewardess":"Malini","Stewardess":"Mala" }
#First element in every pair is the key and the second element is the value.

Accessing the value using key-
crew_details["Pilot"]	                  #This will return the corresponding value for the specified key

Iterating through the dictionary-
for key,value in crew_details.items():
     print(key,":",value)	                #items function gives both key and value, which can be used in a for loop.

'''
#Creating a dictionary
crew_details={
            "Pilot":"Kumar",
            "Co-Pilot":"Raghav",
            "Head-Strewardess":"Malini",
            "Stewardess":"Mala"
}
print(crew_details["Pilot"])

print("\nIterating the dictionary using items function")
for key,value in crew_details.items():
    print(key,":",value)


#Usually while working with dictionary, you will be interested in specific values. 
#Let’s find the value of all pilots from crew_details.
print("\nIterating the dictionary using keyword 'in'")
for key in crew_details:
    if(key=="Pilot" or key=="Co-Pilot"):
        print(crew_details[key])
#Note: Dictionary being unordered, the order of the values being displayed may vary during each execution of the above for loop.

#Dictionaries are mutable
crew_details["Pilot"]="James" # Here the value for key "Pilot" is being updated to "James"
print("\nAfter modifying the value of Pilot:", crew_details["Pilot"])

'''
Kumar

Iterating the dictionary using items function
Pilot : Kumar
Head-Strewardess : Malini
Co-Pilot : Raghav
Stewardess : Mala

Iterating the dictionary using keyword 'in'
Kumar
Raghav

After modifying the value of Pilot: James
'''
