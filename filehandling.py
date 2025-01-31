filename=input("Enter a file name:")
file=open(filename)
text=file.read()
print(type(text))
text=text.lower()
words=text.split()
dup=[]
for i in words:
    if i not in dup:
        dup.append(i)
dup.sort()
print(dup)


