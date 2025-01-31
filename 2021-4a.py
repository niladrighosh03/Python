filename=open('hey.txt')
file=filename.read()
print(file)

char=len(file)
word=len(file.split())
word_c=file.split()
line=file.count('\n')+1
print(char,word,line)

c=[]
for i in set(word_c):
    x=file.count(i)
    if(x>1):
        c.append(i)

print(c)