num=9
i=0
while i<=2:
    x=int(input("Guess: "))
    i+=1
    if x==num:
        print("Win!")
        #break #terminate from loop
else: #while can have else part but its optional like if
    print("Sorry you failed")