command="" #empty string
started=False
while True: 
    command=input("> ").lower() #convert to lower char
    if command =="start":
            if started:
                print("Car is already started")
            else:
                started=True
                print("car started")    
    elif command =="stop":
        if not started:
            print("Car is already stopped")
        else:
            started=False
            print("Car stopped")
    elif command=="help":
        print('''
start-Start the car
        stop-to stop the car 
quit-to quit
        ''') #1st &r3rd line get no space but 2nd line has space
    elif command=="quit":
        break
    else: #it will run for the while loop also
        print("Cant understand")