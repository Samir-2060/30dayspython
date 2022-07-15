#1) Write a Python program to count the number of characters (character frequency) in a string. Sample String : 'google.com'
#=>
string="google.com"
char={} 
for i in string:
    if i in char:
        char[i] +=char[i]
    else:
        char[i] =1
print("The character count in the google.com is:" + str(char))

#2) Write a Python program to get a string made of the first 2 and the last 2 chars
#from a given a string. If the string length is less than 2, return instead of the empty string.

def stringFunction(string):
    if len(string)<2:
        return ""
    else:
        return string[0:2] + string[-2:]
print(stringFunction("python"))

#3.) Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
  #program1:
string="nabeen"
c=string[0] + string[1:].replace(string[0],"$")
print(c)

program2:
test_str = 'google googly'
res = test_str.replace(test_str[0], "$").replace("$", test_str[0], 1)
print("Replaced String : " + str(res))

#program3:
def test_string(string):
    return string[0] + string[1:].replace(string[0],"$")


print(test_string("google googly"))


#4.) #Write a Python program to add 'ing' at the end of a given string (length should
#be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.
string=input("Enter the first string:")
if string.endswith("ing")==True:
    print(string + "ly")
elif len(string)<3:
    print(string)
else:
    print(string + "ing")
    
    
#program2
#Write a Python program to add 'ing' at the end of a given string (length should
#be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.
string=input("Enter the first string:")
if len(string)>2:
    if string[-3:]=="ing":
        string+='ly'
        print(string)
    elif string[-3:]!="ing":
        string+="ing"
        print(string)
    else:
        print(string)
        
        
#5.) #Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com' 

string="google.com"
count_string={}
for i in string:
    if i in count_string:
        count_string[i] +=1
    else:
        count_string[i]=1
print(count_string)


#6.) #Write a Python program to get a string made of the first 2 and the last 2 chars
#from a given a string. If the string length is less than 2, return instead of the
#empty string.

def two_character(string):
    if len(string)<2:
        return " "
    else:
        return string[:2] + string[-2:]
print(two_character("Nirmal"))

#7.) #Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.

def stringinput(string):
    return string[0] + string[1:].replace(string[0],"#")
print(stringinput("sashi"))

#8.) #Write a Python program to get a single string from two given strings, separated
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


#9.) #Write a Python program to find the first appearance of the substring 'not' and
#'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#substring with 'good'. Return the resulting string.

string=input("Enter the string")
snot=string.find("not")
spoor=string.find("poor")
if spoor>snot and snot>0 and spoor>0:
    string=string.replace(string[snot:(spoor+4)],"good")
    print(string)
else:
    print(string)

   program2:
    
  def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

#10. ) #Write a Python program to find the first appearance of the substring 'not' and
#'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#substring with 'good'. Return the resulting string.

string=input("Enter the string")
snot=string.find("not")
spoor=string.find("poor")
if spoor>snot and snot>0 and spoor>0:
    string=string.replace(string[snot:(spoor+4)],"good")
    print(string)
else:
    print(string)

   program2:
    
  def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

#11.) #Write a Python function that takes a list of words and returns the length of the longest one

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

12.) #Write a Python program to remove the nth index character from a nonempty string

def removeindex(string,n):
    first_part=string[:n]
    second_part=string[n+1:]
    return first_part+second_part
print(removeindex("Python",2))
print(removeindex("samir",0))
print(removeindex("bishal",3))

13.) #Write a Python program to change a given string to a new string where the first
#and last chars have been exchanged.

def exchange(string):
    return string[-1:]+string[1:-1] +string[:1]
print(exchange("hello"))
print(exchange("python"))

14.) #Write a Python program to remove the characters which have odd index
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

15.) #Write a Python program to count the occurrences of each word in a given sentence

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

#program2
#Write a Python program to count the occurrences of each word in a given sentence

def count_string(string):
    counts=dict()
    words=string.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(count_string("hello my name is my name"))

16.) #Write a Python script that takes input from the user and displays that input
#back in upper and lower cases.

user_input = input("What's your favorite fruit? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())


#program2:
user_input = input("What's your favorite fruit? ")
upper=user_input.upper()
lower=user_input.lower()
print(upper)
print(lower)

17).#Write a Python function to create the HTML string with tags around the word(s).

#program1
#def add_tags(tag,word):
 #   return "<%s>%s<%s>" %(tag,word,tag)
#print(add_tags('b','python'))

#program2
tag=input("Enter the htm tag")
word=input("Enter the word")
result= "<%s>%s<%s>" % (tag,word,tag)
print(result)

18.) #Write a Python program that accepts a comma separated sequence of words
#as input and prints the unique words in sorted form (alphanumerically).

items=input("Enter the words separated by comma")
word=sorted(set(items.split(",")))
print(word)

19.) #Write a Python program to get the largest number from a list.

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

20.) #Write a Python function to insert a string in the middle of a string.
def insert_string_middle(string,word):
    return string[:2]+word+string[2:]

print(insert_string_middle("<<>>","Pro Programmer"))

21.) #Write a Python program to multiplies all the items in a list
def multiple_list(lst):
    multiple=1
    for i in lst:
        multiple*= i
    return multiple
lst=[1,2,3,4]
print(multiple_list(lst))

22.) #Write a Python program to get the smallest number from a list.

def smallest_list(num):
    smallest=num[0]
    for i in num:
        if i<smallest:
            smallest=i
    return smallest
print(smallest_list([2,4,5,6,342,231,23]))

#program2
#Write a Python program to get the smallest number from a list.

def smallest_list(num):
    num.sort()
    return num[0]
print(smallest_list([45,78,4,2,3]))

#program3
#Write a Python program to get the smallest number from a list.

def smallest_list(num):
    smalllest=min(num)
    return smalllest
print(smallest_list([3,4,5,5,6,2,56,1]))

23.) #Write a Python program to sum all the items in a list.
def sum_list(lst):
    sum_numbers = 0
    for x in lst:
        sum_numbers += x
    return sum_numbers
lst=[1,2,3]
print(sum_list(lst))
# Write a Python script to add a key to a dictionary

def add_dict(dict):
    dict.update({2: 30})
    return dict

print(add_dict({0: 10, 1: 20}))
 

25.) #Write a Python program to check a list is empty or not.

def check(lst):
    if lst==[]:
        print("yes the list is empty")
    else:
        print("No this is non empty list")
(check([]))

26.) #Write a Python program to check whether all dictionaries in a list are empty or not.

def check_dict(lst):
    re=all(not d for d in lst)
    return re
print(check_dict([{},{},{1,2,3}]))

27.) #Write a Python program to clone or copy a list.

def copylist(lst):
    lst2=lst.copy()
    return lst2
print(copylist([1,2,3,4,5]))

28.) #Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given list of strings.

def string_result(lst):
    same=0
    for i in lst:
        if len(i)>=2 and i[0]==i[-1]:
            same+=1
    return same
print(string_result(['abc', 'xyz', 'aba', '1221']))

28.) #Write a Python program to get a list, sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.

def last(n):
	return n[-1]
def sort(tuples):
	return sorted(tuples, key=last)
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sort(a))

29.) #Write a Python program to get a list, sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.

def last(n):
	return n[-1]
def sort(tuples):
	return sorted(tuples, key=last)
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sort(a))

30.) #Write a Python program to insert a given string at the beginning of all items in a list.

def insert_beginning(list,string):
    string += '{0}'
    list = [string.format(i) for i in list]
    return (list)
lst=[1,2,3,4]
str="emp"
print(insert_beginning(lst,str))

31.) #Write a Python program to remove duplicates from a list.

def remove_duplicate(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicate(['a','b','c','b','a','d','a']))

32.) #Write a Python program to replace the last element in a list with another list.

def replace_list(lst1,lst2):
    lst1[-1:]=lst2
    return lst1
lst1=[1, 3, 5, 7, 9, 10]
lst2=[2, 4, 6, 8]
print(replace_list(lst1,lst2))

33.) #Write a Python script to check whether a given key already exists in a dictionary

def checkkey(key,d):
    if key in d:
        print("Key is present in a dictionary")
    else:
        print(("Key is not present in a dictionary"))
checkkey(1,{1: 10,2: 20, 3: 30, 4: 40, 5: 50, 6: 60})

#program2

#Write a Python script to check whether a given key already exists in a dictionary

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_exist(key):
    if key in d:
        print("Key already exist")
    else:
        print("Key doesnot exist")
is_key_exist(4)

34.) #Write a Python script to generate and print a dictionary that contains a
#number (between 1 and n) in the form (x, x*x).

def dictionaries(n):
    d=dict()
    for x in range(1,n+1):
        d[x]=x*x
    return d

print(dictionaries(5))

35.)  #Write a Python program to iterate over dictionaries using for loops.

def dictionaries(dict):
    for key,value in dict.items():
        print(key,":",value)
dictionaries({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

36.) #1) Write a Python program to count the number of characters (character frequency) in a string. Sample String : 'google.com'
#=>
string="google.com"
char={} 
for i in string:
    if i in char:
        char[i] +=char[i]
    else:
        char[i] =1
print("The character count in the google.com is:" + str(char))

#2) Write a Python program to get a string made of the first 2 and the last 2 chars
#from a given a string. If the string length is less than 2, return instead of the empty string.

def stringFunction(string):
    if len(string)<2:
        return ""
    else:
        return string[0:2] + string[-2:]
print(stringFunction("python"))

#3.) Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
  #program1:
string="nabeen"
c=string[0] + string[1:].replace(string[0],"$")
print(c)

program2:
test_str = 'google googly'
res = test_str.replace(test_str[0], "$").replace("$", test_str[0], 1)
print("Replaced String : " + str(res))

#program3:
def test_string(string):
    return string[0] + string[1:].replace(string[0],"$")


print(test_string("google googly"))
