weight=int(input('Enter Weight: '))
unit=input('(L)bs or (K)g    ')
if unit.upper=="L":
    con=weight*0.45
    print(f"Weight in Kg is {con}")
else:
    con=weight/0.45
    print(f"Weight in pound is {con}")