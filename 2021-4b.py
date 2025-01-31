filen=open('hey.txt')
file=filen.read()
content=file.split()

res=[]
for word in content:
    if word[0].isupper() and word[-1].islower():
        for i in word:
            if i=='^':
                res.append(word)
print(res)