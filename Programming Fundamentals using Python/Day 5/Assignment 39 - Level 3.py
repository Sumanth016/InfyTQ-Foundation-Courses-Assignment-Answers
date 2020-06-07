#PF-Assgn-39
#This verification is based on string match.     
#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]
#quantity_available=[2,200,250,3]

def place_order(*item_tuple):
    item_tuple = list(item_tuple)
    
    while len(item_tuple) != 0:
        index = 0
        available = False
        for item in menu:
            if item == item_tuple[0]:
                available = check_quantity_available(index,item_tuple[1])
                if available == True:
                    print("{} is available".format(item_tuple[0]))
                else:
                    print("{} stock is over".format(item_tuple[0]))
                break
            index += 1
        if len(menu) == index:
            print("{} is not available".format(item_tuple[0]))
        del item_tuple[:2] 

def check_quantity_available(index,quantity_requested):
    if quantity_available[index] >= quantity_requested:
        quantity_available[index] = quantity_available[index] - quantity_requested
        return True
    else:
        return False

place_order("Fried Rice",2,"Soup",1)
#place_order("Veg Roll",2,"Noodles",2)

'''
Fried Rice is available
Soup stock is over

'''
