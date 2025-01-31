import random #check modules in External Libraries folder.
for i in range(3):
    print(random.random()) #rendom generates random number between 0 & 1
    print(random.randint(10,20)) #for a specific range

member=['John','Marrry',"Mosh",'Charles']
print(random.choice(member)) #from a list