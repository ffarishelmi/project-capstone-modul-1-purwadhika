from tabulate import tabulate
from .validasi_input import *
from .data import data

def filter_data():
    global data
    while True:
        cari_data = validasi_input_huruf("Mau cari apa? ").capitalize()
        simpan_pencarian = []
        for i in data:
            for key, value in i.items():
                if cari_data in str(value):
                    simpan_pencarian.append(i)
                    break
        if simpan_pencarian:
            print(tabulate(simpan_pencarian, headers="keys", tablefmt="pretty"))
            break
        else:
            print("Data tidak ditemukan")