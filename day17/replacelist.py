#Write a Python program to replace the last element in a list with another list.

def replace_list(lst1,lst2):
    lst1[-1:]=lst2
    return lst1
lst1=[1, 3, 5, 7, 9, 10]
lst2=[2, 4, 6, 8]
print(replace_list(lst1,lst2))
