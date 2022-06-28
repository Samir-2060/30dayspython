#Write a Python program to get the largest number from a list.

def largest_number(number):
    largest=number[0]
    for i in number:
        if i>largest:
             largest=i
    return largest
print(largest_number([6,1,2,3,4,50,40,5]))
