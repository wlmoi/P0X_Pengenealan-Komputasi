# P02_16523109_02
# NIM/Nama: 16523109/William Anthony
# Fakultas: STEI-R
# Tanggal: 05-10-2023
# Kelas: 4.3.b
# Deskripsi: Program membuat sebuah barisan bilangan yang dimulai dari angka 1.

# KAMUS
# X = Integer
# Y = Integer

# ALGORITMA
# INPUT
X = int(input("Masukkan x: "))
Y = int(input("Masukkan y: "))
# PROSES DAN OUTPUT
GY = Y # SIMPAN NILAI Y AWAL
C = 1
A = 1
for i in range(X):
    print(C, end=" ") 
    if C == Y: # JIKA SAMPAI DI Y
        A *= -1
        Y += GY
    elif C == 1:
        A = 1
    C += A
    if C == 0:
        C = 1
