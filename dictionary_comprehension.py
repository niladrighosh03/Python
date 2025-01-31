#dic={0:"item0", 1:"item1"....}, we can make manually by typing the dictionary or do using list comprehension

dic={i:f"Here item{i}" for i in range (5)}
dic1={value:key for key,value in dic.items()} #reverse dic
print(dic)
print(dic1)