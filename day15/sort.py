#Write a Python program that accepts a comma separated sequence of words
#as input and prints the unique words in sorted form (alphanumerically).

items=input("Enter the words separated by comma")
word=sorted(set(items.split(",")))
print(word)
