name=(input("Enter the name"))
if len(name)<5:
    print("name must be atleast 5 characters")
elif len(name)>50:
    print("name can't be greater than 50 characters")
else:
    print("name looks good")

