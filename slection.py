print('Selamat datang di quizz Gamess')
print('Mohon untuk menjawab soal-soal berikuut dengan benar')
print('Jika soal yang anda Jawab Benar anda akan mendapatkan point 20 setiap soal')
print('Jawab soal ketik y/n\ny = benar\nn = salah')
soal_a = str(input('1. Apakah tumbuhan membutuhkan air dan sinar Matahari: '))
soal_b = str(input('2. Ayam termasuk mamalia: '))
soal_c = str(input('3. Hewan Karnivora adalah hewan pemakan daging: '))
soal_d = str(input('4. 1 + 1 = 7: '))
soal_e = str(input('5. Manusia pasti Berak: '))

point = 0
if soal_a == 'y':
    point += 20
    print('Soal 1: Benar')
elif soal_a != 'y':
    print('Soal 1: Salah')

if soal_b == 'n':
    point += 20
    print('Soal 2: Benar')
elif soal_b != 'n':
    print('Soal 2: Salah')

if soal_c == 'y':
    point += 20
    print('Soal 3: Benar')
elif soal_c != 'y':
    print('Soal 3: Salah')

if soal_d == 'n':
    point += 20
    print('Soal 4: Benar')
elif soal_d != 'n':
    print('Soal 4: Salah')

if soal_e == 'y':
    point += 20
    print('Soal 5: Benar')
elif soal_e != 'y':
    print('Soal 5: Salah')
print('----------------')
print('point anda ', point)
if point >= 85:
    print("Anda Lulus")
elif point < 85:
    print('Coba Lagii')