#Write a Python program to count the occurrences of each word in a given sentence

def occurrences(string):
    count=dict()
    words=string.split()

    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word]=1
    return count
print(occurrences("Hello I am live on youtube I am streaming now"))
