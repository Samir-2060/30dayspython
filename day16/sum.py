#Write a Python program to sum all the items in a list.
def sum_list(lst):
    sum_numbers = 0
    for x in lst:
        sum_numbers += x
    return sum_numbers
lst=[1,2,3]
print(sum_list(lst))



