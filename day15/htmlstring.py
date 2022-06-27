#Write a Python function to create the HTML string with tags around the word(s).

#program1
#def add_tags(tag,word):
 #   return "<%s>%s<%s>" %(tag,word,tag)
#print(add_tags('b','python'))

#program2
tag=input("Enter the htm tag")
word=input("Enter the word")
result= "<%s>%s<%s>" % (tag,word,tag)
print(result)
