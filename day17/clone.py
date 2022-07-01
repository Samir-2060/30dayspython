#Write a Python program to clone or copy a list.

def copylist(lst):
    lst2=lst.copy()
    return lst2
print(copylist([1,2,3,4,5]))
