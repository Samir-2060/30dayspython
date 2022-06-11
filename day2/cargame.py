#program 1
initial = input(">")
if initial.upper()=="HELP":
    print("Start- To start the car")
    print("Stop- To stop the car")
    print("Quit-To exit")

if initial=="start":
    print("The car is started")
elif initial=="stop":
    print("The car is stopped")
elif initial=="quit" :
    print('car game exit')
else:
    print("something went wrong")
    
    #program 2
    command=""
while True:
    command=input(">").lower()
    if command=="start":
        print("car is started")
    elif command=="stop":
        print("car is stopped")
    elif command=="help":
        print("""
        Start-To start the car
        stop-To stop the car
        quit-To exit 
        """)
    elif command=="quit":
        break
    else:
        print("Something went wrong")
