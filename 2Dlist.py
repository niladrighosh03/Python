list_2d=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
        ]
print(list_2d)
print(list_2d[0]) #[1, 2, 3]
print(list_2d[0][2]) #3
list_2d[0][2]=87
print(list_2d[0][2]) #87
#print all items
print("All items")
for row in list_2d:
    for i in row:
        print(i)