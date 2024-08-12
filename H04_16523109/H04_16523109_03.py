# H04_16523109_03
# NIM/Nama  : 16523109/William Anthony
# Tanggal   : 24-10-2023
# Kelas     : 4.3.b
# Deskripsi : Program untuk menghitung kapal musuh yang ada.

# KAMUS
# N = int (baris peta)
# M = int (kolom peta)
# PTI = string (Peta saat itu)
# Peta = list of string (Bentuk Peta)
# KP = int (Kapal Perang)
# JKP = int (Jumlah Kapal Perang)

# ALGORITMA          
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))
Peta = [[0 for jedagjedug in range(M)] for _uwu_ in range(N)]
print("Masukkan peta:")
for i in range(N):
    PTI = input() #ASUMSIKAN INPUT BENAR
    for jedagjedug in range(M):                   # Buat barisan jedagjedug (Kolom Peta) 
        Peta[i][jedagjedug] = int(PTI[jedagjedug])   # Buat menjadi integer yang bekerja seperti boolean!

# ALGORITMA MENENTUKAN KAPAL PERANG
JKP = 0   
for i in range(N):                  #   Baris
    for j in range(M):              #           Kolom
        if Peta[i][j] == 1:
            KP = 1      #             Dia merupakan kapal perang
            if (i>0 and Peta[i-1][j] == 1) or (j>0 and Peta[i][j-1] == 1):  
                KP = 0  #             Jika dia terhubung dengan kapal perang lainnya maka bukan
            JKP += KP
     
if JKP != 0: #  Jika terdapat
    print(f"Terdapat {JKP} kapal musuh pada peta")
else: #         JKP == 0
    print("Tidak terdapat kapal musuh pada peta")
