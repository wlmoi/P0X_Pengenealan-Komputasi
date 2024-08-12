# H04_16523109_02
# NIM/Nama  : 16523109/William Anthony
# Tanggal   : 24-10-2023
# Kelas     : 4.3.b
# Deskripsi : Program untuk menentukan jumlah bakteri tersebut ketika ditinggal Nona Deb selama K detik

# KAMUS
# N = int (Jumlah bakteri awal)
# K = int (Jumlah rasio yang akan diberikan)

# ALGORITMA
def jumlah_bakteri(N, K):
    # Def untuk mencari Jumlah Bakteri, Menggunakan rumus sederhana barisan geometri
    return N*(2**(K + 1)-1)

N = int(input("Masukkan N: ")) # I N P U T
K = int(input("Masukkan K: ")) # I N P U T        
print(f"Terdapat {jumlah_bakteri(N, K)} Bakteri Pengkombacter.")  # O U T P U T

    