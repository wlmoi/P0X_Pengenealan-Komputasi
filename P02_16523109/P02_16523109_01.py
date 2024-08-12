# P02_16523109_01
# NIM/Nama: 16523109/William Anthony
# Fakultas: STEI-R
# Tanggal: 05-10-2023
# Kelas: 4.3.b
# Deskripsi:  Program untuk menentukan berapa banyak kegiatan yang bisa dilaksanakan dalam 1 hari dan banyak kegiatan setiap gedung.

# KAMUS
# N = integer
# Peserta = integer
# ALGORITMA
# INPUT
N = int(input("Masukkan nilai N: "))
Ke = 1
B = 0
A = 0
# PROSES
A = 5 # Kapasitas maksimal gedung A
B = 3 # Kapasitas maksimal gedung B
CA = 0
CB = 0
Looping = True
i = 1 #SIKLUS BERAWAL DARI PERTAMA
while Looping:
    Peserta = int(input(f"Masukkan peserta kegiatan ke-{i}: "))
    if Peserta < N and CA < A:
        CA += 1
    elif CB < B:
        CB += 1
    else:
        Looping = False
    i += 1

print(f"Terdapat {CA} kegiatan di gedung A dan {CB} kegiatan di gedung B.")
    

