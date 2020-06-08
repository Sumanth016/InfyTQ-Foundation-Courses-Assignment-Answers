import re

def max_frequency_word_counter(data):
    data_dict = {}
    word = ""
    frequency = 0
    data = re.sub(r",", "", data).lower()
    while data:
        temp = data.split()
        for word in temp:
            count = temp.count(word)
            if len(data_dict) == 0:
                data_dict.update({word: count})
                prev = word
            else:
                if count >= data_dict.get(prev):
                    data_dict.update({word: count})
                    prev = word 
            temp1 = re.sub(r"\b(?=\w)" + re.escape(word) + r"\b(?!\w)","", data)
            data = re.sub(r"  ", " ", temp1).strip()
            break
    maxx = 0
    prev = ''
    for key, value in data_dict.items():
        if value == maxx:
            if len(key) > len(prev):
                maxx = value 
                word = key 
                frequency = value 
                prev = key
            else:
                wordd = prev 
        elif value > maxx:
            maxx = value
            wordd = key
            frequency = value
            prev = key
    print(wordd, frequency)

data = "Work like you do not need money, love like you have never you been hurt, and dance like no one is watching"
max_frequency_word_counter(data)

'''
like 3
'''
'''
you 3
'''
