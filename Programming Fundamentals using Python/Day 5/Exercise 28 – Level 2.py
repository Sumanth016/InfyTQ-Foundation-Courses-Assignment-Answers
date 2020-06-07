#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    count=0
    s={}
    ru=set(match_tuple)
    for j in ru:
        count=0
        for i in match_tuple:
            if(j==i):
                count+=1
        s[j]=count
    if(s["Team1"]>s["Team2"]):
        return "Team1"
    elif(s["Team1"]<s["Team2"]):
        return "Team2"
    else:
        return "Tie"
        
    
#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))

#Team2
