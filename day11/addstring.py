#Write a Python program to add 'ing' at the end of a given string (length should
#be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.
string=input("Enter the first string:")
if string.endswith("ing")==True:
    print(string + "ly")
elif len(string)<3:
    print(string)
else:
    print(string + "ing")
    
    
#program2
#Write a Python program to add 'ing' at the end of a given string (length should
#be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.
string=input("Enter the first string:")
if len(string)>2:
    if string[-3:]=="ing":
        string+='ly'
        print(string)
    elif string[-3:]!="ing":
        string+="ing"
        print(string)
    else:
        print(string)





