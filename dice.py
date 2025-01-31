import random
#one more line break of class
class dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second #python get this a s tuple as we want to do

d1=dice()
print(d1.roll())
