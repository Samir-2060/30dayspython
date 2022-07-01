#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given list of strings.

def string_result(lst):
    same=0
    for i in lst:
        if len(i)>=2 and i[0]==i[-1]:
            same+=1
    return same
print(string_result(['abc', 'xyz', 'aba', '1221']))


