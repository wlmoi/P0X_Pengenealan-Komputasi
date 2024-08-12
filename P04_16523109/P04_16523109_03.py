# P04_16523109_03
# NIM/Nama      : 16523109/William Anthony
# Fakultas      : STEI-R
# Tanggal       : 02-11-2023
# Kelas/Shift   : 4.3.b
# Deskripsi     : Program untuk mengidentifikasi apakah pion Raja putih aman dari serangan pion Kuda hitam

# KAMUS
# m = integer 
# pc = list of list of string (papan catur)
# ASUMSI INPUT SESUAI TEST CASE !!!
# 
# # ALGORITMA
def gpionkuda(m, pc):
    # FUNGSI untuk meninjau gerakan kuda (MENGELUARKAN OUTPUT)
    for i in range(m):
        for j in range(m):
            if pc[i][j] == "K":
                if i-2 >= 0 and j-1 >= 0 and pc[i-2][j-1] == "R":   # TINJAU GERAKAN KUDA
                    return False
                if i-2 >= 0 and j+1 < m and pc[i-2][j+1] == "R":    # YANG KAYAK L (2(x)+ y)
                    return False
                if i+2 < m and j-1 >= 0 and pc[i+2][j-1] == "R":    # DAN (x + 2(y))
                    return False
                if i+2 < m and j+1 < m and pc[i+2][j+1] == "R":     # DIMANA NILAI x dan y bisa bernilai
                    return False
                if i-1 >= 0 and j-2 >= 0 and pc[i-1][j-2] == "R":   # POSITIF ATAU NEGATIF (Kanan Atas vs Bawah Kiri)
                    return False
                if i-1 >= 0 and j+2 < m and pc[i-1][j+2] == "R":    # 
                    return False
                if i+1 < m and j-2 >= 0 and pc[i+1][j-2] == "R":    #
                    return False
                if i+1 < m and j+2 < m and pc[i+1][j+2] == "R":     # 
                    return False
    return True                                                     # Jika Ia tidak diserang maka aman
    
 
m = int(input("Masukkan nilai m: "))
pc = [["" for no3kubenarkankak in range(m)] for terimakasih_untukberikankomentar_agarmenjelaskan in range(m)] #Deklarasi Papan catur
for i in range(m):      # SATU SATUNYA TEST CASE YANG BISA DITIRU
    for j in range(m):  # SOALNYA TEST CASE 2 dan CASE 3 
        pc[i][j] = input(f"Masukkan elemen matriks ke-{i+1} {j+1}: ")

# SEPERTI PADA TEST CASE
print("Hasil papan catur")          # KITA HARUS PRINT DULU PAPAN CATUR BAGAIMANA
for i in range(m):
    for j in range(m):
        print(pc[i][j], end=" ")
    print()
        
if gpionkuda(m, pc): #Jika True (Aman)
    print("Raja aman dari serangan kuda.")
else:                #Jika tidak maka tidak aman
    print("Raja tidak aman dari serangan kuda.")