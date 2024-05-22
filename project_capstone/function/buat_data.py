
from .print_data import *
from .data import data
from .validasi_input import *

data_baru = {"Year": 0, "Product Name": 0, "Category": 0, "Price": 0, "Stock": 0, "Rating": 0, "Seller": 0}

def tambah_data():
    global data, data_baru

    for i in data_baru.keys():
        while True:
            masukan_data = input(f"Masukan data {i}: ").capitalize()
            if i in ["Year", "Price", "Stock"]:
                if masukan_data.isdigit():
                    data_baru[i] = int(masukan_data)
                    break
                else:
                    print(f"{i} tidak valid, input hanya bisa angka")
            elif i == "Rating":
                try:
                    data_baru[i] = float(masukan_data)
                    break
                except ValueError:
                    print(f"{i} tidak valid, input hanya bisa float")
            elif i in ["Category", "Seller"]:
                if masukan_data.isalpha():
                    data_baru[i] = masukan_data
                    break
                else:
                    print(f"{i} tidak valid, input hanya bisa huruf")
            elif i == "Product Name":
                data_baru[i] = masukan_data
                break

    data.append(data_baru)
    data_baru = {"Year": 0, "Product Name": 0, "Category": 0, "Price": 0, "Stock": 0, "Rating": 0, "Seller": 0}
    tampilkan_data(data)