#Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
  program1:
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

