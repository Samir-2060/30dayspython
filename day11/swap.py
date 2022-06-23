#Write a Python program to get a single string from two given strings, separated
#by a space and swap the first two characters of each string.

def two_string(str1,str2):
    x=str1[:2]
    str1=str1.replace(str1[:2],str2[:2])
    str2=str2.replace(str2[:2],x)
    return str1+ " " + str2

print(two_string("abc","xyz"))

#program2:
#Write a Python program to get a single string from two given strings, separated
#by a space and swap the first two characters of each string.
str1=input("Enter the first string:")
str2=input("Enter the second string")
x=str1[:2]
str1=str1.replace(str1[:2],str2[:2])
str2=str2.replace(str2[:2],x)
print(str1+ " " + str2)

