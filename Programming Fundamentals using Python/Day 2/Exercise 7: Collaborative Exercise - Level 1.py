def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=no_of_adults*37550+ no_of_children*(37550/3)
    total_ticket_cost=total_ticket_cost+total_ticket_cost*0.07
    total_ticket_cost*=0.9

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
