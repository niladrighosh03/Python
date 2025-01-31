def emoji(message):
    word =message.split(' ')
    print(word) 
    emoji={
        ":)" :"😁", #happy
        ":(" :"😒" #sad
    }
    op=""
    for i in word:
        op +=emoji.get(i,i) +" "
    return op


msg=input("-> ") #two line leave according to standard
emo=emoji(msg)
print(emo)