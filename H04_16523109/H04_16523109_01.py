# H04_16523109_01
# NIM/Nama  : 16523109/William Anthony
# Tanggal   : 24-10-2023
# Kelas     : 4.3.b
# Deskripsi : Program untuk menentukan jumlah maksimum submatriks berukuran 2 x 2 yang memiliki elemen ganjil.

# KAMUS
# m = int
# n = int
# tabel = list of string
# a = int
# b = int
# c = int
# d = int 
# sum = int
# submatriksganjil = int

# ALGORITMA
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
tabel = [[0 for i in range(n)] for j in range(m)] #Deklarasi
submatriksganjil = 0 #                   Nilai awal
if m == n:  #                            Square dan m == n
    print("Masukkan elemen matriks: ")
    for i in range(m):
        tabelbro = input()           #Menerima input dari barisan ke i
        tabel[i] = tabelbro.split( ) #split dan len diperbolehkan#
else:       #                            Non-Square m != n
    for i in range(m):
        for j in range(n):
            tabel[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))
for i in range(1, m): #               Algoritma mencari jumlah submatriks ganjil maksimum
    for j in range(1, n):
        a = int(tabel[i][j])         # kanan bawah
        b = int(tabel[i-1][j])       # kiri bawah
        c = int(tabel[i][j-1])       # kanan atas
        d = int(tabel[i-1][j-1])      # kiri atas
        if a % 2 != 0 or b % 2 != 0 or c % 2 != 0 or d % 2 != 0: # SEMUANYA GENAP
            sum = a + b + c + d
            if submatriksganjil < sum:
                submatriksganjil = sum
        
if submatriksganjil != 0:
    print(f"Jumlah maksimum dari submatriks 2x2 yang memiliki elemen ganjil adalah {submatriksganjil}")
else:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")
    
    