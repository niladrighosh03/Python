#dictionary is used to store information that comes as key value pairs, like structure in c

#dictionary of a customer
customer={
   "name" : "John", #name is the value
    "age" : 30, #each key value should be unique i.e. we can't use "age" again in our dictionary
    "is_verified" : True
}
print(customer["name"]) #this will return the value associated with it

#print(customer["birthday"])--- we get error here as no key value like that

print(customer.get("Birthady")) #here we dont get error, we get "none". 'None' represents the absence of value

print(customer.get("pin","3456")) #if the value is not present then set deafult value to show

customer["name"]="Stive" #update value
customer["passion"]="cricket" #add new value
print(customer["name"], customer["passion"])