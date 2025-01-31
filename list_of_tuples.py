# create tuples with college id and
# name and store in a list
data = [(1, 'sravan'), (2, 'ojaswi'), (3, 'bobby'),
		(4, 'rohith'), (5, 'gnanesh')] #also can be done using zip & map function

# display data
print(data)


#by user input
n = int(input("Enter the number of tuples: "))
tuple_list = []

for _ in range(n):
    tuple_input = input("Enter the values for the tuple (separated by commas): ")
    values = tuple_input.split(",")
    tuple_list.append(tuple(values))

print("List of tuples:", tuple_list)






#access the tuple & their values
tuple_list = [('a', 1), ('b', 2), ('c', 3)]

# Accessing the first tuple
first_tuple = tuple_list[0]
print(first_tuple)  # Output: ('a', 1)

# Accessing the second value of the second tuple in one line
second_value = tuple_list[1][1]
print(second_value)  # Output: 2






#make the tuples into their original data type i.e. int, float, string, bool. But in the previous input all are considered to be String

n = int(input("Enter the number of tuples: "))
tuple_list = []

for _ in range(n):
    tuple_input = input("Enter the values for the tuple (separated by commas): ")
    values = tuple_input.split(",")

    # Convert values to appropriate data types
    converted_values = []
    for value in values:
        if value.isdigit():
            converted_values.append(int(value))
        elif value.lower() == "true":
            converted_values.append(True)
        elif value.lower() == "false":
            converted_values.append(False)
        else:
            converted_values.append(value)

    tuple_list.append(tuple(converted_values))

print("List of tuples:", tuple_list)