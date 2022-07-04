#1) Write a Python program to count the number of characters (character frequency) in a string. Sample String : 'google.com'
#=>
string="google.com"
char={} 
for i in string:
    if i in char:
        char[i] +=char[i]
    else:
        char[i] =1
print("The character count in the google.com is:" + str(char))

#2) Write a Python program to get a string made of the first 2 and the last 2 chars
#from a given a string. If the string length is less than 2, return instead of the empty string.

def stringFunction(string):
    if len(string)<2:
        return ""
    else:
        return string[0:2] + string[-2:]
print(stringFunction("python"))

#3.) Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
  #program1:
string="nabeen"
c=string[0] + string[1:].replace(string[0],"$")
print(c)

program2:
test_str = 'google googly'
res = test_str.replace(test_str[0], "$").replace("$", test_str[0], 1)
print("Replaced String : " + str(res))

#program3:
def test_string(string):
    return string[0] + string[1:].replace(string[0],"$")


print(test_string("google googly"))


