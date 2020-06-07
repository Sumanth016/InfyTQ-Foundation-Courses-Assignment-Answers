#PF-Assgn-22
def find_leap_years(given_year):
    count=0
    list_of_leap_years=[]
    while(count<15):
        if(given_year%400==0 or (given_year%100!=0 and given_year%4==0 )):
            list_of_leap_years.append(given_year)
            count=count+1
            given_year+=4
        else:
            given_year+=1
    return list_of_leap_years

list_of_leap_years=find_leap_years(2002)
print(list_of_leap_years)
#for i in range(0,15):
 #   print(list_of_leap_years[i])
 
 '''
 #PF-TCV-Assgn-22
import pytest
from <packagename>.solution import function_name

def test_find_leap_years_1():
    result=find_leap_years(2002)
    assert result==[2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]
 '''
