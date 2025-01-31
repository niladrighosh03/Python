
class person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi, I am {self.name}")


jack=person("John smith")
print(jack.name)
jack.talk()

boby=person("Rock")
boby.talk()