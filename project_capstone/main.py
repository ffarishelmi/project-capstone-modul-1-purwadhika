# LIBRARY
import sys, os
from function import *

# MENJALANKAN TABEL DATA DARI AWAL
simpan_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
tampilkan_data(data)
sys.stdout = simpan_stdout

# FUNGSI OPERASI UNTUK DIJALANKAN PENGGUNA ADMIN
def pilihan_menu_admin(prompt):
    while True:
        print_main_menu_admin()
        opsi_menu = input(prompt)
        if opsi_menu == '1':
            tampilkan_data(data)
            break
        elif opsi_menu == '2':
            tambah_data()
        elif opsi_menu == '3':
            perbaharui_data()
        elif opsi_menu == '4':
            hapus_data()
        elif opsi_menu == '5':
            login()
        elif opsi_menu == '6':
            exit()
        else:
            print("Ketik menu rentang 1 sampai 6")

def halaman_admin():
    while True:
        input_awal = pilihan_menu_admin("Pilih Menu ")
        mengulang = ulangi_or_keluar("Ulangi atau keluar? y/n ").lower()
        if mengulang == 'n':
            print("Terimakasih")
            exit()

# FUNGSI OPERASI UNTUK DIJALANKAN PENGGUNA PEMBELI
def pilihan_menu_pembeli(prompt):
    while True:
        print_main_menu_pembeli()
        opsi_menu = input(prompt)
        if opsi_menu == '1':
            lihat_barang()
            break
        if opsi_menu == '2':
            print_keranjang(keranjang)
        elif opsi_menu == '3':
            login()
        elif opsi_menu == '4':
            exit()
        else:
            print("Ketik menu rentang 1 sampai 4")

def lihat_barang():
    while True:
        print('''
Apa yang ingin ditampilkan?
a) Tampilkan semua data
b) Filter data
c) Sorting data
d) Belanja barang
e) Kembali ke halaman sebelumnya
              ''')
        pilih_opsi = validasi_input_huruf("Pilih opsi ").lower()
        if pilih_opsi == 'a':
            tampilkan_data(data)
        elif pilih_opsi == 'b':
            filter_data()
        elif pilih_opsi == 'c':
            sorting_data()
        elif pilih_opsi == 'd':
            tampilkan_data(data)
            masuk_keranjang()
            break
        elif pilih_opsi == 'e':
            return 'e'
        else:
            print("Opsi salah, silahkan ulangi")
            continue
        
        mengulang = ulangi_or_keluar("Ulangi atau keluar? y/n ").lower()
        if mengulang == 'n':
            break

def halaman_pembeli():
    while True:
        input_awal = pilihan_menu_pembeli("Pilih Menu ")
        if input_awal == '1':
            if lihat_barang() == 'e':
                continue
        elif input_awal:
            mengulang = ulangi_or_keluar("Ulangi atau keluar? y/n ").lower()
            if mengulang == 'n':
                print("Terimakasih")
                exit()

# FUNGSI LOGIN
def login():
    while True:
        username = input("Masukan Username: ")
        password = input("Masukan Password: ")
        if username == akun_pembeli[0]["Username"] and password == akun_pembeli[0]["Password"]:
            halaman_pembeli()
            break
        elif username == akun_admin[0]["Username"] and password == akun_admin[0]["Password"]:
            halaman_admin()
            break
        else:
            print("Username atau Password anda salah. Ulangi")

login()