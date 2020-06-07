def encode(message):
    encode = message+"0"
    l=[]
    count = 1
    for index, value in enumerate(encode): 
        if value != "0":
            if value == encode[index+1]:
                count = count+1
            else:
                l.append(str(count))
                l.append(value)
                count=1    
    return "".join(l)
    
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)

#---------------------------------------------------------------------------------

#PF-Assgn-30

def encode(message):
    count=1
    srt=""
    for i in range(len(message)-1):
        if(message[i]==message[i+1]):
            count+=1
        else:
            srt=srt+str(count)+message[i]
            int(count)
            count=1
    if(len(message)==1):
        srt= str(count) +message[0]
    elif(message[i]==message[i+1]):
        
        srt=srt+str(count)+message[i]
        int(count)
        count=1
    else:
        srt=srt+str(count)+message[i+1]
        int(count)
        count=1
    return srt
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
