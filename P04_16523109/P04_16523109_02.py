# P04_16523109_02
# NIM/Nama      : 16523109/William Anthony
# Fakultas      : STEI-R
# Tanggal       : 02-11-2023
# Kelas/Shift   : 4.3.b
# Deskripsi     : Program untuk mengubah sebuah matriks yang berukuran mxn menjadi matriks baru dengan cara yang menarik. 

# KAMUS
# m = int
# n = int
# matriks = list of list of int (matriks yang mulanya)
# matriksbaru = list of list of int (matriks yang ingin dibuat)


# ALGORITMA

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
matriks = [[0 for pengkomNIM16523109harus100 in range (n)] for tolongberikannilaipengkomtinggi in range (m)] # Buat matriks
if m == n:
    print("Masukkan elemen matriks:")
    for i in range(m):
        inputuser = input()
        matriks[i] = inputuser.split( )
else: # m!= n
    for i in range(m):
        for j in range(n):
            matriks[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))
            
matriksbaru = [[0 for praktikumpengkomjanganpelitnilai in range (n)] for terimakasihkak in range(m)]

for i in range(m): # MEMBUAT ALGORITMA UNTUK MENGANTIKAN DENGAN JUMLAH ELEMEN DI KIRI KANAN ATAS BAWAH
    for j in range(n):
        if i > 0:
            matriksbaru[i][j] += int(matriks[i-1][j])
        if i < m-1:
            matriksbaru[i][j] += int(matriks[i+1][j])
        if j > 0:
            matriksbaru[i][j] += int(matriks[i][j-1])
        if j < n-1:
            matriksbaru[i][j] += int(matriks[i][j+1])

print("Matriks baru: ") # MENYIAPKAN OUTPUT
for i in range(m):
    for j in range(n):
        print(matriksbaru[i][j], end=" ")
    print()
    
    