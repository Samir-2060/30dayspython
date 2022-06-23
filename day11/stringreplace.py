#Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.

def stringinput(string):
    return string[0] + string[1:].replace(string[0],"#")
print(stringinput("sashi"))
