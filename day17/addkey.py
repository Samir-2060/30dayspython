# Write a Python script to add a key to a dictionary

def add_dict(dict):
    dict.update({2: 30})
    return dict

print(add_dict({0: 10, 1: 20}))
