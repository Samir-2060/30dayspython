#Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com' 

string="google.com"
count_string={}
for i in string:
    if i in count_string:
        count_string[i] +=1
    else:
        count_string[i]=1
print(count_string)
