from tabulate import tabulate
import random

def tampilkan_data(data):
    random.seed(1)
    for index, nomor in enumerate(data, 1):
        nomor["No"] = index
    for index, keys in enumerate(data, 1):
        keys["Product Id"] = random.randint(10000, 99999)
    print(tabulate(data, headers="keys", tablefmt="pretty"))

# PRINT MENU ADMIN
def print_main_menu_admin():
    print('''
Pilih menu:
1. Tampilkan Stok Barang
2. Tambahkan Barang
3. Perbaharui Data Barang
4. Hapus Data Barang
5. Logout
6. Selesai
          ''')

# PRINT MENU PEMBELI
def print_main_menu_pembeli():
    print('''
Silahkan datang di Toko Elektronik. Pilih menu:
1. Lihat Barang
2. Lihat Keranjang
3. Logout
4. Selesai
          ''')

# FUNGSI MENGULANGI PROGRAM ATAU KELUAR PROGRAM (STOP PROGRAM)
def ulangi_or_keluar(prompt):
    while True:
        output = input(prompt)
        if output == 'y':
            return output
        elif output == 'n':
            return output
        else:
            print("Input hanya bisa y atau n ")
            print("Ulangi")