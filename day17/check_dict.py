#Write a Python program to check whether all dictionaries in a list are empty or not.

def check_dict(lst):
    re=all(not d for d in lst)
    return re
print(check_dict([{},{},{1,2,3}]))
