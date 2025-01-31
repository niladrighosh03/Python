try:
    age=int(input(("Enter age ")))
    risk=2000/age
    print(age)
except ValueError: #also can use except Exception
    print("Value is not in integer") #print(Exception)
except ZeroDivisionError:
    print("Cant devide with zero")