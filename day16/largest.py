#Write a Python program to get the largest number from a list.

def largest_number(number):
    largest=number[0]
    for i in number:
        if i>largest:
             largest=i
    return largest
print(largest_number([6,1,2,3,4,50,40,5]))

#program2
#Write a Python program to get the largest number from a list.

def largest_number(number):
    number.sort()
    return number[-1]

print(largest_number([1,2,3,50,34,40]))

#program3
def largest_number(number):
     result=max(number)
     return result

print(largest_number([1,2,3,50,34,40]))
