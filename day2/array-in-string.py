#Working with array in string
name="my name is samir kc"
print(name[0])  #m

print(name[-1]) #c
print(name[0:7]) #my name
#first character has zero index.In the example string start
# to count from m(index 0) and ends in index 6/e(index 7 is exluded)

print(name[:5])
#if we want to start slicing the string from starting(index 0) to the certain index then we
#can use [:x].

print(name[2:10])
#white space is also character.In this example my is exluded and started to
# count from the whitespace after Y letter of my.So we can see space before "name is" in output.
