class animal:
    def walk(self):
        print("walk")


#pass the name of the parent class in parameter of sub class. So that's how the sub class i.e. Dog class will inherit all the methods of parent class i.e. animal
 
#Python does not like an empty class(class without anything i.e. totally blank, no methods, variable etc.). SO add methods specific to a class or just use "pass" statement in the empty class. Thus our class will have a statement & doesn't become empty

class Dog(animal): 
    pass


class Cat(animal):
    def bark(abc):
        print("drink milk")


d1=Dog()
d1.walk() #using method of parent class
c1=Cat()
c1.bark()