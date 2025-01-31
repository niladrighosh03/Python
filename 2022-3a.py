words=['raj','lol', 'raj', 'hello', 'lol']
dict={}
for i in set(words):
    dict[i]=words.count(i)
print(dict)
# for key, value in dict.items():
#     print(key,value)