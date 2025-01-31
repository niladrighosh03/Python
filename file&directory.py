from pathlib import Path
#pathlib is module & Path is class.(P in capital letter)
#Absolute Path:--From the root directory. Like in windows-  c:\Program Files\Microsoft
#Relative path:-- FRom a purticular directory

p1= Path("Package") #take a directory as an argument
print(p1.exists()) #returns boolean

#create a directoy
p2=Path("Created_Dir")
p2.mkdir() #check directory has been created
#to remove directory use 'p2.rmdir()'

