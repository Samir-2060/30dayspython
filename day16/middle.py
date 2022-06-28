#Write a Python function to insert a string in the middle of a string.
def insert_string_middle(string,word):
    return string[:2]+word+string[2:]

print(insert_string_middle("<<>>","Pro Programmer"))
