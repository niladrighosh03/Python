#item is a variable & for each iteration this item variable will hold one character at a time i.e. --
#for 1st iteration P will print
#for 2nd iteration y will print and so on...
for item in "Python":
    print(item)

for item in ["Raj", "John", "Paul"]:
    print(item)



#range function
y=range(5)
print(y) #range(0, 5)
x=range(2,5)
print(x) #range(2, 5)


n=5
for i in range (n): #range(n) is starting from 0 upto n-1 times
    print(i)
print("Next Loop")
for i in range(3,6):
    print(i)#start from 3 to 5
print(i) #5


print("Next Loop")
for i in range(3,10,2): #we get 2 step forward for the 2
    print(i)