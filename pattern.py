num=[5,2,5,2,2]
for i in num:
    #print('x' * i),without using it
    op=''
    for count in range(i):
        op +='x'
    print(op)