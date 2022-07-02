#Write a Python script to concatenate following dictionaries to create a new one.

def concatenate_dict(dict1,dict2,dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
print(concatenate_dict(dict1,dict2,dict3))


#program2

#Write a Python script to concatenate following dictionaries to create a new one.

def concatenate_dict(dict1,dict2,dict3):
    dict= {**dict1,**dict2,**dict3}
    return dict
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
print(concatenate_dict(dict1,dict2,dict3))

