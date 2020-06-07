def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    count=101
    for i in range (0,no_of_passengers):
        src=source[0:3]
        des=destination[0:3]
        ticket_number_list.append(airline+":"+src+":"+des+":"+str(count))
        count+=1
    if(no_of_passengers<5):
        return ticket_number_list
    else:
        return ticket_number_list[-5:]
print(generate_ticket("AI","Bangalore","London",7))
#Provide different values for airline,source,destination,no_of_passengers and test your program


