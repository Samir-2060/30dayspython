#program1
user=input("Enter the name")
for item in user:
    print(item)
    
#program2
for item in ["nirmal","samir","sachin"] :
    print(item)
    
 #program3
for item in [1,2,3,4]:
    print(item)
    
  #program4
  for item in range(10):
    print(item)
    
  #program5
  for item in range(2,10):
    print(item)
    
    #program6
    for item in range(2,100,4):
    print(item)
    
    #program7
    price=[20,30,40]
total=0
for item in price:
    total+=item
    print(total) #print the value in each iteration
print(f"The total price is {total}") #print the total final price after end of loop
