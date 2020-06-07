#PF-Assgn-26
def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    ans=False  
    #Populate the variables: chicken_count and rabbit_count
    for i in range(heads+1):
        j=heads-i
        if (2*i)+(4*j)==legs:
            chicken_count=i
            rabbit_count=j
            ans=True
            break
    if (ans==True):
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(3,12)
