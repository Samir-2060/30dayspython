#Write a Python function that takes a list of words and returns the length of the longest one

def longestLength(a):
    max1=len(a[0])
    temp=a[0]

    for i in a:
        if len(i)>max1:
            max1=len(i)
            temp=i
    print("The list item with longest length is",temp,"and length of the longest list item is",max1)
a=["apple","banana","mangoes","samir","bishal"]
longestLength(a)
