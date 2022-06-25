#Write a Python program to remove the nth index character from a nonempty string

def removeindex(string,n):
    first_part=string[:n]
    second_part=string[n+1:]
    return first_part+second_part
print(removeindex("Python",2))
print(removeindex("samir",0))
print(removeindex("bishal",3))
