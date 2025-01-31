#emoji convertor
message=input("Enter message with symbol-> ")
word =message.split(' ')
print(word) #when get a space it will slipt the string into list

emoji={
    ":)" :"😁", #happy
    ":(" :"😒" #sad
}
op=""
for i in word:
    op +=emoji.get(i,i) +" " #if the given symbol not in emoji then return that symbol as it is
print(op)