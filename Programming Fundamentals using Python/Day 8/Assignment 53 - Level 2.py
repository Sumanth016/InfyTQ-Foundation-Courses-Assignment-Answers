#PF-Assgn-53
#This verification is based on string match.
import re

poem='''
It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

print(poem.count('v'))
print()
print(re.sub(r'\n',r' ',poem).strip())

print()
temp=re.sub(r"ch",r"Ch",poem)
print(re.sub(r"co",r"Co",temp))

print()
temp=re.sub(r"ai...",r"ai*\*",poem)
print(re.sub(r"hi...",r"hi*\*",temp))

'''
3

It takes strength for being certain, It takes courage to have doubt. It takes strength for challenging alone, It takes courage to lean on another. It takes strength for loving other souls, It takes courage to be loved. It takes strength for hiding our own pain, It takes courage to help if it is paining for someone.


It takes strength for being certain,
It takes Courage to have doubt.
It takes strength for Challenging alone,
It takes Courage to lean on another.
It takes strength for loving other souls,
It takes Courage to be loved.
It takes strength for hiding our own pain,
It takes Courage to help if it is paining for someone.



It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hi*\*g our own pain,
It takes courage to help if it is pai*\*g for someone.


'''
