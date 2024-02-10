# tipe data dictionery seperti object pada js

person = {'name': 'Andryan', 'age': 16, 'kelas' : 11}
print(person)
print(person['name'])

person['alamat'] = 'Bayat'
person['job'] = "front-end engginer"

print(person)

del person['alamat']
person['job'] = "Software Engginer"
print(person)

# merubah ke dictionary
print(dict([[1,2],[3,4]]))