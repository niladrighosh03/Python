#list_methods
num=[3,4,10]
num.append(56) #to add new item into at end of list
print(num)
num.insert(1,78) #at 1 index insert 78
print(num)
num.remove(10) #to remove an item
print(num)

num.pop() #delete item from last
print(num)
print(num.index(78)) #return the index number of 78, but print(num.index(18)) it will give error as 18 is not in the list

print(78 in num) #True--gives boolean value but here we get 'no error'

num=[3,4,10,3,4,1,4]
print(num.count(4)) #3--it gives the frequency of the item

#sort method
num.sort() #sort method--it returns None. None is an object in python that represents the absence of a value. So sort method doestn't return value, it sinply sort the list. Sort list in ascending order
print(num) 

num.reverse() #to get the list in descending order just reverse the list
print(num) 

num2=num.copy() #copy of a list
print(num2)

num.clear() #to clear all items from list
print(num)