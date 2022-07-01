#Write a Python program to insert a given string at the beginning of all items in a list.

def insert_beginning(list,string):
    string += '{0}'
    list = [string.format(i) for i in list]
    return (list)
lst=[1,2,3,4]
str="emp"
print(insert_beginning(lst,str))

