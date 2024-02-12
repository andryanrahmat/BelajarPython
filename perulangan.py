nama = str(input("Masukkan Nama Anda: "))
encode_name = ''

panjang_nama = len(nama)
for i in range(0, panjang_nama):
    encode_name = encode_name + (nama[i]+ str(panjang_nama))

print(encode_name)