#largest no in list
def findmax(num):
    maximum=num[0]
    for i in num:
        if i>maximum:
            maximum=i
    return maximum
