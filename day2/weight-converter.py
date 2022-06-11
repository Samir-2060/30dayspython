weight=float(input("Enter the weight"))
unit=input("want to convert in (L)bs or (K)g:")
if unit=="L" or unit=="l":
    unit2= weight *2.205
    print(f"you are {unit2} pound")
elif unit=="K" or unit=="k":
    unit2=weight*0.4535
    print(f"You are {unit2} Kg")
else:
    print("something went wrong in very wrong way")

    
#program 2
weight=float(input("Enter the weight"))
unit=input("want to convert in (L)bs or (K)g:")
if unit.upper()=="L":
    unit2= weight *2.205
    print(f"you are {unit2} pound")
elif unit.upper()=="K":
    unit2=weight*0.4535
    print(f"You are {unit2} Kg")
else:
    print("something went wrong in very wrong way")
