#string_method
s='Hi Jon'
print(len(s)) #len includes the space also
o1=s.upper() #upper case
print(o1) #HI JON
print(s+',---Not mutable') #s is not mutable----Hi Jon

x=s.find('i') #return the index only
print(x)
print(s.find('z')) #z is present so return -1
print(s.find("Jon")) #J start at index 3
print(s.replace('Jon',"Smith")) #case sensative
print(s) #Hi Jon, as s is not mutable

print('J' in s)   #it means  J is present in string s, it returns boolean value while find return the index
print('HEllo' in s) #flase, as HEllo is not in s