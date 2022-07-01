#Write a Python program to remove duplicates from a list.

def remove_duplicate(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicate(['a','b','c','b','a','d','a']))
