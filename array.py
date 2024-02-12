import array

# my_array = [65,2,5,6,2,23,3543,5,3534,2,32,3,53,4,6,54,5,2,3,23,5,43443534,434,24,23,2,32,234343,43434325657,657678,7,879673453,4345465475674,2342,34353464623564,6547,658685674635,3432]
# left_pointer = my_array[0]


# for i in range(1, len(my_array)):
#     right_pointer = my_array[i]
#     if right_pointer > left_pointer:
#         left_pointer = right_pointer


# print(left_pointer)





# array = [1,3,21,4,54,32,34,43,34,3,54,56,567,76,67,56,56,67,3,23,312,23,564,567,564,34]
# left = array[0]

# for x in range(1,len(array)):
#     right = array[x]
#     if right > left:
#         left = right
# print(left)


print("# mencari rata rat pada sebuah array")
list_number = [i for i in range(501)]
print(list_number)

total = 0
for x in range(0,len(list_number)):
    total += x
print(total)

result = total // len(list_number)
print(result)


print("Mencari element tertinggi di sebuah array")

number = [7827,2,3,5,4,3,34,45,6,32,465,32,23,23,565367,3223523,235634,234356,23436,2,3345,54,63,36423,4]

left_pointer = number[0]

for i in range(1, len(number)):
    right_pointer = number[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

print("mencari nilai terendah di dalam array")

for i in range(1,len(number)):
    right_pointer = number[i]
    if right_pointer < left_pointer:
        left_pointer = right_pointer
print(left_pointer)
