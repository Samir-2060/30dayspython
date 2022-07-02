   #Write a Python program to iterate over dictionaries using for loops.

def dictionaries(dict):
    for key,value in dict.items():
        print(key,":",value)
dictionaries({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
