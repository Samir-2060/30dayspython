#Write a Python program to multiplies all the items in a list
def multiple_list(lst):
    multiple=1
    for i in lst:
        multiple*= i
    return multiple
lst=[1,2,3,4]
print(multiple_list(lst))

