ph=input("Enter phonr number ")
# "1" -> "one"
#use dictionary
map={
    "1":"one",
    "2":"two",
    "3":"three" #dont write all
}
op=""
for i in ph:
    op+=map.get(i,"Not get!")+ " "
print(op)