#Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'
#=>
string="google.com"
char={}
for i in string:
    if i in char:
        char[i] +=char[i]
    else:
        char[i] =1
print("The character count in the google.com is:" + str(char))

