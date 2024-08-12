def perkalian_angka(b):
    # Fungsi yang kalikan digit setiap digit dari bilangan tersebut secara berulang kali hingga hanya tersisa 1 digit saja
    # proses = int
    # b = bilangan = string/int
    # h = int (Hasil)
    
    proses = 0
    while len(b) > 1:
        h = 1
        for digit in b:
            h *= int(digit)
        b = str(h)
        proses += 1
        print(f"Setelah proses ke-{proses} : {h}")

# Menerima masukan sebuah bilangan
b = input("Masukkan sebuah bilangan : ")
perkalian_angka(b)
