
# KAMUS
# M = int (Baris)
# N = int (Kolom)
# matriks = list of list of int
# banyak_perubahan = int
# i = int (index in for used for rows)
# j = int (index in for used for coloums)
# baris = int
# perubahan = string
# kolom = int

def urutkan_baris(matriks, baris, N):
    # Sorting rows (Ganti kalau misalnya yg sebelum lebih besar)
    for i in range(N):
        for j in range(i+1, N):
            if matriks[baris][i] > matriks[baris][j]:
                matriks[baris][i], matriks[baris][j] = matriks[baris][j], matriks[baris][i]

def urutkan_kolom(matriks, kolom, M):
    # Sorting coloums (Ganti kalau misalnya yg sebelum lebih besar)
    for i in range(M):
        for j in range(i+1, M):
            if matriks[i][kolom] > matriks[j][kolom]:
                matriks[i][kolom], matriks[j][kolom] = matriks[j][kolom], matriks[i][kolom]

# Menerima masukan ukuran matriks
M = int(input("Masukkan nilai M: "))
N = int(input("Masukkan nilai N: "))
matriks = [[0 for i in range (N)] for reivan in range (M)] # matrics of int
# Menerima masukan elemen matriks jika tidak berbentuk persegi (Test case 1 n 2)
if M != N:
    for i in range(M):
        baris = input().split()
        for j in range(N):
            baris[j] = int(baris[j])
        matriks += [baris]
else: # M == N
    for i in range(M):
        for j in range(N):
            matriks[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

# Menerima banyak perubahan
banyak_perubahan = int(input("Banyak Perubahan : "))

for i in range(banyak_perubahan):
    # CEK INPUT
    perubahan = input(f"Perubahan Ke-{i+1}: ")
    
    if perubahan == "baris":
        # Menerima baris yang diubah dan mengurutkannya gunakan algoritma sorting
        baris = int(input("Masukkan baris yang diubah : ")) - 1 #Biar in range
        urutkan_baris(matriks, baris, N) # Menerapkan fungsinya menggunakan variabel matriks,baris,N
    elif perubahan == "kolom":
        # Menerima kolom yang diubah dan mengurutkannya gunakan algoritma sorting
        kolom = int(input("Masukkan kolom yang diubah : ")) - 1 # Ini juga untuk mengambil matriksnya
        urutkan_kolom(matriks, kolom, M) # Menerapkan fungsinya menggunakan variabel itu

# Menampilkan hasil matriks akhir
for i in range(M):
    baris = '' # Siapin setiap barisan biar nanti di print seolah printer
    for j in range(N): #    Di setiap column
        baris += str(matriks[i][j]) + ' ' #print di awal "baris" dan matriks yang sudah terurut
    print(baris)
