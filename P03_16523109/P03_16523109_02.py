# P02_16523109_02
# NIM/Nama: 16523109/William Anthony
# Fakultas: STEI-R
# Tanggal: 19-10-2023
# Kelas/Shift: 4.3.b
# Deskripsi: Program untuk menentukan jumlah potongan list yang jika seluruh elemen penyusun potongannya dijumlahkan akan menghasilkan bilangan prima.

# KAMUS
# JBA = integer (Jumlah Bilangan Asli)
# BA = list of integer ("Bilangan Asli")
# JPL = int (Jumlah Potongan List)
# JBE = int (Jumlah Bilangan Elemen)
# AP = boolean (Apakah Prima)
# Looping = boolean (Untuk membuat siklus looping algoritma)

# ALGORITMA
JBA = int(input("Masukkan jumlah bilangan asli: ")) # Input
BA = [0 for i in range(JBA)] # Deklarasi BA
JPL = 0                      # Deklarasi BA
# PROSES MULAI
for i in range(JBA):
    BA[i]= int(input(f"Masukkan bilangan asli ke {i+1}: ")) 

for i in range(JBA):
    for j in range(i, JBA):
        JBE = 0
        for k in range(i, j+1):
            JBE += BA[k]
        if JBE > 1:
            AP = 1 
            Looping = True # Algoritma akan diciptakan
            l = 2 # Membantu mengecek apakah merupakan bilangan prima
            while Looping and l < JBE:
                if (JBE % l) == 0:
                    AP = 0
                    Looping = False
                l += 1
            if AP: # Jika AP = 1 Maka merupakan angka prima
                JPL += 1 # Tambah jumlah potongan
# SET UP OUTPUT
if JPL>0:
    print("Terdapat", JPL , "potongan list yang jumlahnya prima.")
else: #JPL != 0
    print("Tidak ada potongan list yang jumlahnya prima.")
