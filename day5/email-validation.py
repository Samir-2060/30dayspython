email=input("Enter the Email:")
k,j,d=0,0,0
if len(email)>6: #1
    if email[0].isalpha(): #2
        if ("@" in email) and (email.count("@")==1): #3
            if (email[-4]==".") ^ (email[-3]=="."): #4
                for i in email:
                   if i==i.isspace(): #5
                       k=1
                   elif i.isalpha():#5
                       if i==i.upper():
                           j=1
                   elif i.isdigit():
                       continue
                   elif i == "_" or i == "." or i == "@":
                       continue
                   else: #5
                       d=1
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email 5")

            else:
                print("Invalid email 4")
        else:
            print("invalid email 3")
    else:
        print("Invalid email 2")
else:
    print("Invalid Email 1")
