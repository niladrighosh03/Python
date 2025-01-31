class Point:
    def __init__(self,x,y): #inti is for initialized, reffered as constructor. So constructor name must be __init__(self, argument)
        self.x=x
        self.y=y


    def move(self): 
        print('move')

    def draw(self):
        print('draw')

p1=Point(10,20)
p1.k=11
print(p1.x,p1.k)