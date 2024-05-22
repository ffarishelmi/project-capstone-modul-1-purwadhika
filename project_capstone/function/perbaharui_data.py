from .data import *
from .print_data import *
from .validasi_input import *

kolom_data = list(data[0].keys())

def perbaharui_data():
    global data, data_baru, kolom_data
    
    while True:
        tampilkan_data(data)
        baris_data = validasi_input_angka("Data keberapa yang ingin diubah? ")
        baris_data -= 1
        for i, j in enumerate(data):
            if baris_data == i:
                while True:
                    pilih_data = validasi_input_huruf("Data apa yang ingin diubah? ")
                    pilih_data = pilih_data.title()
                    if pilih_data in ["Year", "Price", "Stock"]:
                        update = validasi_input_angka("Masukan data: ")
                        data[baris_data][pilih_data] = update
                        tampilkan_data(data)
                        konfirmasi = validasi_input_huruf("Apa masih ada data yang ingin diubah? y/n ").lower()
                        if konfirmasi == 'n':
                            tampilkan_data(data)
                            break
                    elif pilih_data == "Rating":
                        pilih_data = float(pilih_data)
                        update = validasi_input_angka("Masukan data: ")
                        data[baris_data][pilih_data] = update
                        tampilkan_data(data)
                        konfirmasi = validasi_input_huruf("Apa masih ada data yang ingin diubah? y/n ").lower()
                        if konfirmasi == 'n':
                            tampilkan_data(data)
                            break
                    elif pilih_data in ["Category", "Seller"]:
                        update = validasi_input_huruf("Masukan data: ")
                        update = update.title()
                        data[baris_data][pilih_data] = update
                        tampilkan_data(data)
                        konfirmasi = validasi_input_huruf("Apa masih ada data yang ingin diubah? y/n ").lower()
                        if konfirmasi == 'n':
                            break
                    elif pilih_data == "Product Name":
                        update = input("Masukan data: ")
                        update = update.title()
                        data[baris_data][pilih_data] = update
                        tampilkan_data(data)
                        konfirmasi = validasi_input_huruf("Apa masih ada data yang ingin diubah? y/n ").lower()
                        if konfirmasi == 'n':
                            break
                break
            elif baris_data > len(data):
                print("Kolom data tidak tersedia, silahkan ketik ulang")
        break