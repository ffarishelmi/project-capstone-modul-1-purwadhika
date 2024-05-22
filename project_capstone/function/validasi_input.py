def validasi_input_huruf(cek):
    while True:
        huruf = input(cek)
        cek_huruf = huruf.replace(" ", "")
        if cek_huruf.isalpha():
            return huruf
        else:
            print("Input tidak valid, hanya bisa huruf. Ulangi")

def validasi_input_angka(cek):
    while True:
        angka = input(cek)
        if angka.isdigit():
            return int(angka)
        else:
            print("Input tidak valid, hanya bisa angka. Ulangi")