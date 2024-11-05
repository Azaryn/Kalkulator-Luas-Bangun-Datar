print(""" Selamat Datang di Kalkulator Luas Bangun Datar
1. Persegi panjang
2. Jajar genjang
3. Persegi
4. Segitiga
5. Lingkaran
6. Kembali ke menu awal  
""")

def persegi_panjang(x,y): 
    return x * y #mengembalikan nilai dari fungsi dan nilai yang dikembalikan adalah hasil dari operasi x kali y

def jajar_genjang(x,y):
    return x * y #mengembalikan nilai dari fungsi dan nilai yang dikembalikan adalah hasil dari operasi x kali y

def persegi(x):
    return x * x #mengembalikan nilai dari fungsi dan nilai yang dikembalikan adalah hasil dari operasi x kali x

def segitiga(x,y):
    return (1/2) * x * y #mengembalikan nilai dari fungsi dan nilai yang dikembalikan adalah hasil dari operasi setengah x kali y

def lingkaran(r):
    return 3.14 * (r ** 2) #mengembalikan nilai dari fungsi dan nilai yang dikembalikan adalah hasil dari operasi phi (3,14) kali jari jari pangkat 2

while True:
    print("Selamat datang di Kalkulator King Athar!!!")
    choice = int(input("Silahkan pilih (1/2/3/4/5): "))
    if choice in (1,2,3,4,5):

        if choice == 1:
            try:
                num1 = int(input("Masukkan Panjang: "))
                num2 = int(input("Masukkan Lebar: "))
            except ValueError:
                print("Masukkan angka dengan benar!!")
            print(f"{num1} * {num2} = ",persegi_panjang(num1,num2))

        elif choice == 2:
            try:
                num1 = int(input("Masukkan Alas: "))
                num2 = int(input("Masukkan Lebar: "))
            except ValueError:
                print("Masukkan angka dengan benar!!")
            print(f"{num1} * {num2} = ", jajar_genjang(num1,num2))

        elif choice == 3:
            try:
                num1 = int(input("Masukkan Sisi: "))
            except ValueError:
                print("Masukkan Angka dengan benar")
            print(f"{num1} * {num1} = ",persegi(num1))

        elif choice == 4:
            try:
                num1 = int(input("Masukkan Alas: "))
                num2 = int(input("Masukkan Tinggi: "))
            except ValueError:
                print("Masukkan Angka dengan benar")
            print(f" 1/2 * {num1} * {num2} = ",segitiga(num1,num2))

        elif choice == 5:
            try:
                num1 = int(input("Masukkan Jari jari: "))
            except ValueError:
                print("Masukkan Angka dengan benar")
            print(f"3,14 * {num1}^2 = ",lingkaran(num1))