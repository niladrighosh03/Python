def even(num,x): #'num' is parameter, which we define in function for receiving information
    if (num%2!=0):
        print(f"{num} is Odd & {x} is variable")
    else:
        print(f"{num} even & {x} is variable")

n=8
x=even(n,"Any variable pass here") #'n' is argument is actual pieces of information that we supply to these functions. (its Positional Arguments)
#parameter & arguments are different
