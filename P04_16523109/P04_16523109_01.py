# P04_16523109_01
# NIM/Nama      : 16523109/William Anthony
# Fakultas      : STEI-R
# Tanggal       : 02-11-2023
# Kelas/Shift   : 4.3.b
# Deskripsi     : Program untuk membantu para asisten praktikum menilai tugas praktikan 

# KAMUS 
# soal_1 = integer
# soal_2 = integer
# soal_3 = integer
# a = float
# b = float
# c = float

# ALGORITMA
def cekvalid(soal_1, soal_2, soal_3):
    # Fungsi untuk mengecek apakah nilai soal valid atau tidak, Disebut fungsi karena mengeluarkan output!!! (Return)
    if soal_1 < 0 or soal_2 < 0 or soal_3 < 0:
        return False
    elif soal_1 > 100 or soal_2 > 100 or soal_3 > 100:
        return False
    else: 
        return True

def hitung(soal_1, soal_2, soal_3, a, b, c):    #hitung akan menerima 6 buah bilangan
    # Fungsi untuk menghitung semua apabila valid, Disebut fungsi karena mengeluarkan output!!! (Return)
    if a<0 or a>1 or b<0 or b>1 or c<0 or c>1:
        return "bobot tidak valid"
    if a+b+c != 1:                       # Jika bobot tidak valid maka begini
        return "bobot tidak valid"
    if cekvalid(soal_1, soal_2, soal_3): # Jika valid (melewatkan cekvalid)
        nilai_tugas = a*soal_1 + b*soal_2 + c*soal_3 # Tidak harus .00 
        return nilai_tugas

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
soal_1 = int(input("Masukkan nilai soal 1: "))
soal_2 = int(input("Masukkan nilai soal 2: "))
soal_3 = int(input("Masukkan nilai soal 3: "))

print(hitung(soal_1, soal_2, soal_3, a, b, c)) # Kedua fungsi digunakan pada program utama!!!
