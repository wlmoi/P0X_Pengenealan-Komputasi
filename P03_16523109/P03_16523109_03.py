# P02_16523109_03
# NIM/Nama: 16523109/William Anthony
# Fakultas: STEI-R
# Tanggal: 19-10-2023
# Kelas/Shift: 4.3.b
# Deskripsi: Program untuk memeriksa apakah tulisan Komi sudah benar atau belum.

# KAMUS
# PKA = int
# KA = string
# MPKD = int
# MKD = string
# MKD_YangBenar = string 

# ALGORITMA
# INPUT
PKA = int(input("Masukkan panjang kata asli: "))
KA = input("Masukkan kata asli: ")
MPKD = int(input("Masukkan panjang kata yang ditulis: "))
MKD = input("Masukkan kata yang ditulis: ")
# PROSES DAN OUTPUT
if MPKD < PKA:
    print("Tulisan Komi masih salah.")
else:
    MKD_YangBenar = "" 
    for i in range(PKA): 
        for j in range(i+1):
            MKD_YangBenar += KA[j] 
    if MKD_YangBenar == MKD: 
        print("Tulisan Komi sudah benar.")
    else:
        print("Tulisan Komi masih salah.")
