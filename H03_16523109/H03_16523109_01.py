# H03_16523109_01
# NIM/Nama: 16523109/William Anthony
# Tanggal: 12-10-2023
# Kelas: 4.3.b
# Deskripsi: Program untuk menentukan nomor-nomor perwakilan yang tidak mendatangi acara tersebut secara terurut naik.

# KAMUS
# N = int
# M = int
# TABEL = list of int 
# MASUK = int (Nomor Perwakilan yang mendatangi)

# ALGORITMA
N = int(input("Masukkan nilai N: "))                    # Input N
M = int(input("Masukkan nilai M: "))                    # Input M
TABEL = [i+1 for i in range(N)]                         # DEKLARASI ARRAY TABEL
for i in range(M):                                      # !| DISINI KITA MENYIAPKAN ALGORITMA MENCARI YANG MENGHADIRI|!
    MASUK = int(input(f"Masukkan data ke-{i+1}: "))     # MEMASUKKAN NILAI
    for i in range(N):
        if MASUK == TABEL[i]:                           # MENCARI APABILA TERDAPAT NILAI MAKA MENGHADIRI,
            TABEL[i] = False                            # SEHINGGA AKAN DITANDAI DENGAN NILAI FALSE PADA i DISAAT ITU
print(f"Nomor perwakilan yang tidak datang: ", end="")  # !| DISINI KITA MENYIAPKAN OUTPUT |!
for i in range(N):
    if TABEL[i] == False:                               # KETIKA PADA ARRAY URUTAN i adalah False,
        print("", end="")                               # MAKA NOMOR TERSEBUT DILEWATKAN
    else:                                               # SEHINGGA PROGRAM AKAN MENCETAK SEMUA NOMOR
        print(TABEL[i], end=" ")                        # PERWAKILAN YANG TIDAK DATANG SECARA TEURUT NAIK

