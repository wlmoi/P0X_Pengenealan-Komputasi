# P02_16523109_03
# NIM/Nama: 16523109/William Anthony
# Fakultas: STEI-R
# Tanggal: 05-10-2023
# Kelas: 4.3.b
# Deskripsi: Program yang membuat piramida bilangan dengan beberapa ketentuan khusus.

# KAMUS
# P = integer (Panjang Piramida)
# S = integer (Selisih Bilangan Piramida)

# ALGORITMA
# INPUT
P = int(input("Masukkan panjang piramida: "))
S = int(input("Masukkan selisih: "))
# PROSES DAN OUTPUT
A = 1 # Nilai Awal
if P%2 == 0:
   PA = (P//2) #Panjang AKhir
else:
    PA = (P//2)+2
for i in range(PA): # ATAS KEBAWAH
    for j in range(i,PA-1): # X KIRI
        print("X",end="")
    for j in range(2*i+1): # BILANGAN
        print(A, end="")
    for j in range(i,PA-1): # X KANAN
        print("X",end="")
    
    A += S
    while A>=10:
        A-=10
    print()
    