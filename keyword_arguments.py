def even(num,x):
    if (num%2!=0):
        print(f"{num} is Odd & {x} is variable")
    else:
        print(f"{num} even & {x} is variable")

n=8
x=even(x="Any variable pass here",num=n)  #order does not matter in argument
x=even(n, x="Next we can use keyword arguments after positional")