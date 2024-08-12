# H03_16523109_02
# NIM/Nama: 16523109/William Anthony
# Tanggal: 12-10-2023
# Kelas: 4.3.b
# Deskripsi: Program untuk menentukan nilai terbesar ke-N 

# KAMUS
# Data = int
# N = int
# BD = list of int (BANYAK DATA)

# ALGORITMA
Data = int(input("Masukkan banyak data: "))                              # !| I N P U T |!
N = int(input("Masukkan nilai N: "))                                     # DATA, N, DAN BD
BD = [int(input(f"Masukkan data ke-{i+1}: ")) for i in range(Data)]      # BANYAK DATA
for i in range(Data):                                                    # !| P R O S E S|!
    for j in range(Data):                                                # MEMBUAT ALGORITMA YANG MENGURUTKAN
        if BD[i]>BD[j-1]:                                                # URUTAN BANYAK DATA BERDASARKAN
            x = BD[i]; BD[i] = BD[j-1]; BD[j-1] = x                      # BILANGAN TERBESAR (Swap jika nilai indeks tersebut lebih besar)
print(f"Nilai terbesar ke-{N} adalah {BD[N-1]}")                         # !| O U T P U T |!