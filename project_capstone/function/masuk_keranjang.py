from .validasi_input import *
from .lihat_keranjang import *
from .data import data

keranjang = []

def masuk_keranjang():
    global data, keranjang
    isi_keranjang = [{"Product Name": item["Product Name"], "Price": item["Price"], "Seller": item["Seller"]} for item in data]
    while True:
        print('''
Silahkan masukan barang ke keranjang terlebih dahulu
            ''')
        ketemu = False
        while True:
            respon_user = input("\n\nKetik nomor barang atau nama barang: ").strip()
            tanya_jumlah = validasi_input_angka("Berapa jumlah barang yang ingin di beli? ")
            if respon_user.isdigit():
                respon_user = int(respon_user)
                respon_user -= 1
                for i, j in enumerate(data):
                    if respon_user == i:
                        ketemu = True
                        if tanya_jumlah <= data[i]["Stock"]:                    
                            keranjang.append(isi_keranjang[i])
                            nomor = len(keranjang) - 1
                            keranjang[nomor]['Jumlah'] = tanya_jumlah
                            print_keranjang(keranjang)
                            data[i]["Stock"] -= tanya_jumlah
                        elif tanya_jumlah > data[i]["Stock"]:
                            stok_tersedia = data[i]["Stock"]
                            print(f"Stok hanya tersisa {stok_tersedia}")
                if ketemu == False:
                    print('''Barang yang anda cari tidak ditemukan.
Ketik nomor data berdasarkan yang ada di tabel.\n''')
                
            elif respon_user.isalpha() or " " in respon_user:
                respon_user = respon_user.title()
                for index, value in enumerate(data):
                    if respon_user == value["Product Name"]:
                        keranjang.append(isi_keranjang[index])
                        nomor = len(keranjang) - 1
                        keranjang[nomor]['Jumlah'] = tanya_jumlah
                        print_keranjang(keranjang)
                        if tanya_jumlah <= data[i]["Stock"]:
                            data[i]["Stock"] -= tanya_jumlah 
                        else:
                            stok_tersedia = data[i]["Stock"]
                            print(f"Stok hanya tersisa {stok_tersedia}")
                if ketemu == False:
                    print('''Barang yang anda cari tidak ditemukan.
Ketik nama produk berdasarkan yang ada di tabel.
                            ''')
            break

        tanya_kembali = validasi_input_huruf("Apakah masih ada barang yang ingin anda tambahkan? y/n \n\n").lower()
        if tanya_kembali == 'n':
            return 0