s="Father's name"
e='My "Father"'
d='''hey
how are 
you'''
print(s,e,d)

##manipulation with strings
s1='Python for yours'
   #012345  --index 
print(s1[0]) #P
print(s1[-1]) #s, index of last char
print(s1[-2]) #r, 2nd last char
print(s1[0:3]) #including index from 0 but excluding 3 i.e. upto 2---output 'Pyt'
print(s1[0:]) #print from starting to last
print(s1[1:]) #excluding 1st character & print till end
print(s1[:5]) #by deafult start index is 0 & print till 4th(5-1) index----Pytho


s2=s1[:]#copy whole thing
print(s2)

s3="Rajes"
   #01234
 #-5-4-3-2-1  --index
print(s3[1:-1]) #print from 1st index i.e. 2nd position to exclude last char i.e. -1 index char -----aje