# H03_16523109_03
# NIM/Nama: 16523109/William Anthony
# Tanggal: 12-10-2023
# Kelas: 4.3.b
# Deskripsi: Program untuk menentukan stasiun sebagai tempat memulai perjalanan dan banyaknya stasiun yang Tuan Leo kunjungi.

# KAMUS
# Uang = int
# ST = int
# HS = list of int (harga Uang)
# KSS : int
# KSS_UrutanAwal : list of int
# LetakStasiun : int
# sum : int

# ALGORITMA
#                                                              !|  INPUT  |!
Uang = int(input("Masukkan uang yang dibawa Tuan Leo: "))    # Uang yang dibawa Tuan Leo
ST = int(input("Masukkan jumlah stasiun: "))                 # Stasiun Terdata (Jumlah Stasiun)
HS = [(int(input(f"Masukkan harga stasiun ke-{i+1}: "))) for i in range(ST)] # HARGA STASIUN
#                                                 !| P R O S E S   D A N   O U T P U T    |!
#                                      !|  Algoritma mencari stasiun awal dan banyak stasiun yang dikunjungi  |!

if ST == 1:  
    KSS_UrutanAwal = [0 for i in range(ST+1)]     #        TROUBLESHOOT KASUS LANGKA DIMANA HANYA ADA 1 STASIUN SAJA
                                                  #        Hal ini terjadi karena algoritma perulangan untuk mencari letak stasiun
                                                  #        akan berkendala jika tidak ada indeks yang didepan indeks awal. Jika                                     
else:                                             #        ST != 1, maka algoritma perulangan bekerja.
    KSS_UrutanAwal = [0 for i in range(ST)]       #         !|        Deklarasi letak stasiun awal              |!
                                                      #      | Merupakan Array agar dapat menentukan letaknya   |      
for i in range(ST):         #                   !|PENGULANGAN SEBANYAK JUMLAH STASIUN|!
    LetakStasiun = i        #              Letak Stasiun untuk menentukan nilai Array HS yang dipakai
    sum = 0                 #``````````````````````````````````````````````````````````````````````````````````               
    KSS = -1                #                        Kunjung Stasiun Sebanyak..?
    while Uang >= sum and KSS<ST:           #       Ketika uang masih dapat dikurangkan (sum/total biaya lebih kecil sama dengan uang),
        sum += HS[LetakStasiun]              #      Maka dimasukkan dalam algoritma untuk menentukan berapa kali dia kunjung stasiun
        KSS += 1                              #     Setiap pengurangan uang bermakna bahwa ia mengunjung stasiun sekali
        LetakStasiun = (LetakStasiun + 1) % ST #    Ketika sudah sampai ST (Banyak Stasiun), Kembali ke stasiun awal)
            
    # Mencari stasiun awal (Harus didalam algoritma agar dapat menentukan letaknya dimana saat berpindah-pindah)
    if KSS > KSS_UrutanAwal[1]:     #               Memeriksa apakah rute sebelumnya (Siklus while Uang tadi) lebih efektif daripada
        KSS_UrutanAwal[0] = i+1     #               yang sebelumnya. Jika tidak, maka diganti.
        KSS_UrutanAwal[1] = KSS     #               Stasiun Awal paling efektif (Ditambah 1 karena phyton array selalu bermula dari 0)

#  Ketika tidak kunjung sama sekali     !| Menentukan output dari kasus tidak ada kunjung stasiun    |!
if KSS == 0: 
    print("Tuan Leo kekurangan uang.")
else:  # KSS != 0                       !|   Menentukan output dari kasus ada kunjung stasiun        |!
    print(f"Tuan Leo dapat mengunjungi {KSS_UrutanAwal[1]} stasiun dimulai dari stasiun ke-{KSS_UrutanAwal[0]}")