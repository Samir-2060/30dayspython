#Program 1: app.py
from utils import find_max

numbers=[1,2,34,56,23,12]
max=find_max(numbers)
print(max)

#utils.py
def find_max(numbers):
    max=numbers[0]
    for number in numbers:
        if number>max:
            max=number
    return max
