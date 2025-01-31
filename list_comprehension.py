#list comprehension in python
#divisor of 3 using normal for loop
ls=[]
for  i in range(10):
    if i%3==0:
        ls.append(i)
print(ls)

#do this thing using list comprehension
lis=[i for i in range(10) if i%3==0] #I need the value of 'i' in the list called 'lis'. 'i' can be got by the for loop with the condition
print("Using list comprehension ",lis)