#class in Python
#we use classes to define new types
#like using list we can use 'append', 'clear', 'find' etc. So here we wanna make our methods by using class

#1st letter(P) is in capital, its called pascal naming convention. So the naming convention we use for naming our class is different from the convention we use for naming our variables, functions. Here in class name we use capital letters to separe word (AccountDetails)dont use underscore(Account_Details)

#'self' is reference to the current object
class Point:
    def move(self): #must be a parameter while using a method inside of class
        print('move')

    def draw(abc): #instead of self you can use anything but there must be a parameter
        print('draw')

p1=Point()  #creating object p1
p1.draw() 
p1.x=10 #x is attribute
print(p1.x)
p1.move()