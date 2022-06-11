i=1
while i<=3:
    user=int((input("Guess:")))
    print(user)
    i=i+1
    if user==9:
        print("your guess is right")
    else:
        print("your guess is wrong")
    
#program 2 : Here we are treating input string as string and proceeding.

i=1
while i<=3:
    user=(input("Guess:")))
    print(user)
    i=i+1
    if user=="9": #treating 9 as string taken from user
        print("your guess is right")
    else:
        print("your guess is wrong")
        
        
 #program 3: for Clear variable declaration
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess_number=int(input("Guess:"))
    guess_number += 1
    if guess_number==secret_number:
        print("Your guess is correct")
    else:
        print("you failed to guess correct")
