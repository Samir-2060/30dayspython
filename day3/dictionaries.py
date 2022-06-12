customer={
    "name" :"samir",
    "age" : 19,
    "address": "kohalpur,Banke"
}
customer["name"]= "bishal"
print(customer.get("name"))
customer["birthdate"] = "26 Nov 2003"
print(customer["birthdate"])


#program 2
phone=input("Phone number:")
digit_mapping={
   "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6": "six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output=""
for ch in phone:
    output +=digit_mapping[ch]
print(output)

#program 3
phone=input("Phone number:")
digit_mapping={
   "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6": "six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output=""
for ch in phone:
    output +=digit_mapping[ch] + " "
print(output)

#program 4
phone=input("Phone number:")
digit_mapping={
   "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6": "six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output=""
for ch in phone:
    output +=digit_mapping.get(ch,"!") + " "
print(output)
