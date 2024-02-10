
# Mutable

my_name = ['Andryan', 'Zulfi', 'Rahmat']

my_name.append('Tri')
my_name.append('Saputra')

print(my_name)

# imutable

text = 'Hello Andryan'
print(id(text))

text = 'Hi Zulfii'
print(id(text))
print(text)


#  + menambahkan dua list yang berbeda

first_name = ['Andryan', 'Zulfi']
last_name = ['Rahmat', 'Tri', 'Saputra']

full_name = first_name + last_name

print(full_name)


# extend Menambahkan list atau item dibelakangnya
list_1 = [1,2,3,4]
list_2 = ['a','b','c']
list_1.extend(list_2)
print(list_1)

# del Menghapus item yang kita inginkan
dec_list = [1,2,3,4,5,6,7,8,9,10,11]
del dec_list[6]

print(dec_list)

# pop untuk menghapus item terakhir

n_list = [10,20,30]
print(n_list) # print seluruh items

n = n_list.pop(0)
print('n = ',n)
print('n_list =',n_list)

# remove untuk menghapus nilai tertentu

n_list = [11,22,33,44,55,66]
print(n_list)

n_list.remove(44)
print(n_list)

