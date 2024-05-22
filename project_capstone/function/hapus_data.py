from .print_data import *
from .validasi_input import *
from .data import data

def hapus_data():
    global data, data_baru

    while True:
        tampilkan_data(data)
        pilih_data = validasi_input_angka("Data ke berapa yang ingin dihapus? ")
        if pilih_data <= len(data):
            del data[pilih_data - 1]
            tampilkan_data(data)
            break
        else:
            print("Data tidak ada, ulangi")