#Write a Python script to check whether a given key already exists in a dictionary

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
