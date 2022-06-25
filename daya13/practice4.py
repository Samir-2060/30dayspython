#Write a Python program to remove the characters which have odd index
#values of a given string.

def removeodd(string):
    result=""
    for i in range(len(string)):
        if i%2==0:
            result=result+string[i]
    return result

print(removeodd("hello"))

#program2:
def excludeodd(string):
    result=""
    for i in range(len(string)):
        if i%2==0:
            result=result+string[i]
    return result
print(excludeodd("hello I am learning python live in youtube streaming"))
