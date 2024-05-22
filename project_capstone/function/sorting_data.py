from tabulate import tabulate
from .validasi_input import *
from .data import data

def sorting_data():
    global data
    while True:
        pilih_kolom = validasi_input_huruf('''
    Apa yang mau diurutkan?
    - Year
    - Product Name
    - Category
    - Price
    - Stock
    - Rating
    - Seller
    ketik nama kolom: ''')
        pilih_kolom = pilih_kolom.title()
        daftar_kolom = ["Year", "Product Name", "Category", "Price", "Stock", "Rating", "Seller"]
        if pilih_kolom in daftar_kolom:
            pilih_urutan = validasi_input_huruf('''
                    Urutkan berdasarkan apa?
                    ketik 'a'(ascending) atau 'd'(descending) 
                    ''').lower()
            if pilih_urutan == 'a':
                sorting_data = sorted(data, key=lambda x: x[pilih_kolom])
                tabel_data = tabulate(sorting_data, headers="keys", tablefmt="pretty")
                print(tabel_data)
                break
            elif pilih_urutan == 'd':
                sorting_data = sorted(data, key=lambda x: x[pilih_kolom], reverse=True)
                tabel_data = tabulate(sorting_data, headers="keys", tablefmt="pretty")
                print(tabel_data)
                break
        else:
            print("Input tidak valid. Ulangi")