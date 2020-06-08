#PF-Assgn-61
import re
def validate_name(name):
    #Start writing your code here
    if len(name)>0 and len(name)<16 and name.isalpha():
        return True
    else:
        return False
 
def validate_phone_no(phno):
    #Start writing your code here
    phnoset=list(set([i for i in phno]))
    if phno.isdigit() and len(phno)==10 and len(list(phnoset))!=1:
        return True
    else:
        return False
 
def validate_email_id(email_id):
    if re.match(r"\w+@(gmail|yahoo|hotmail)\.com",email_id):
        return True
    else:
        return False
    #Start writing your code here
 
def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    flag=0
    if validate_name(name):
        flag=1
    else:
        print("Invalid Name")
        return
    if validate_phone_no(phone_no):
        flag=2
    else:
        print("Invalid phone number")
        return
    if validate_email_id(email_id):
        flag=3
    else:
        print("Invalid email id")
        return
    if flag==3:
        print("All the details are valid")
 
 
#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")

# All the details are valid
