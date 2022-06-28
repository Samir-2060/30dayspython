#Write a Python program to get the smallest number from a list.

def smallest_list(num):
    smallest=num[0]
    for i in num:
        if i<smallest:
            smallest=i
    return smallest
print(smallest_list([2,4,5,6,342,231,23]))

#program2
#Write a Python program to get the smallest number from a list.

def smallest_list(num):
    num.sort()
    return num[0]
print(smallest_list([45,78,4,2,3]))

#program3
#Write a Python program to get the smallest number from a list.

def smallest_list(num):
    smalllest=min(num)
    return smalllest
print(smallest_list([3,4,5,5,6,2,56,1]))
