# P02_16523109_01
# NIM/Nama: 16523109/William Anthony
# Fakultas: STEI-R
# Tanggal: 19-10-2023
# Kelas/Shift: 4.3.b
# Deskripsi: Program untuk menentukan berapa banyak uang yang harus dia keluarkan untuk makan di restoran tersebut jika dia akan makan selama 3 jam

# KAMUS
# N = integer (Akan selalu diatas 3 karena "Mereka buka selama N jam (lebih dari 3 jam)")
# HJ = list of integer (Harga )
# MinJam = integer (Minimal Jam)
# TH_Looping = integer (Total Harga dalam iterasi)
# ALGORITMA
N = int(input("Masukkan nilai N: "))
HJ = [0 for i in range(N)] # Deklarasi
for i in range(N):
    HJ[i]= int(input(f"Masukkan harga jam ke-{i+1}: ")) 

MinJam = HJ[0] + HJ[1] + HJ[2]  # buat nilai awal minjam

for i in range(1, N-2):  # LOOPING
    TH_Looping = HJ[i] + HJ[i+1] + HJ[i+2]
    if TH_Looping < MinJam:
        MinJam = TH_Looping

print("Total harga yang harus dibayar adalah "+str(MinJam)+".")
