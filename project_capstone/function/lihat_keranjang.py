from tabulate import tabulate

def print_keranjang(keranjang):
    if keranjang:
        print(tabulate(keranjang, headers="keys", tablefmt="pretty"))
        total = 0
        for i in keranjang:
            harga_barang = i["Price"] * i["Jumlah"]
            total += harga_barang
        print(f"Total harga belanja anda: Rp.{total}\n")
    else:
        print("Keranjang belanja anda kosong.")