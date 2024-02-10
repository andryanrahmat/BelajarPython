#Iterator
# list
list_number = [2,6,1,0,4,9]
print(list_number * 2)

# tuples

tupl_number = (1,2,3,4,5) * 3
print(tupl_number)

# string

str_name = 'Andryan '
print(str_name *5)

# range
range_numbers = list(range(6)) * 4
print(range_numbers)

# Count Method
list1 = [2,2,2,1,1,23,4,3,2,45,53]
print(list1.count(2))

tup1 = (3,2,3,40,2,33,2,2,34,4,4,4,3,2,4,4,2)
print(tup1.count(4))

str1 = "Zulfiiii"
print(str1.count('i'))

range_2 = range(0,10,1)
print(len(range_2))
print(range_2.count(5))


# linking menggabungkan antara tipe data yang sama 

# list
first_name = ['Andryan']
last_name = ['Zulfi']

full_name = first_name + last_name
print(full_name)

# tuples
tupl_number1 = (1,2,3,4,5)
tupl_number2 = (6,7,8,9,10)
print(tupl_number1 + tupl_number2)

# string 
my_name = 'Zulfi '
your_name = 'Tri'

print(my_name + your_name, 'loveee')

# range 
range_1 = tuple(range(20)) + tuple(range(20, 30))
print(range_1)


# Operators
