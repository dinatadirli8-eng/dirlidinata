
print("====================================")
print("       KASIR KANTIN KAMPUS")
print("====================================")

total_belanja = 0

while True:
    nama = input("\nMasukkan nama makanan (ketik selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    harga = int(input("Masukkan harga makanan: Rp"))
    jumlah = int(input("Masukkan jumlah pembelian: "))

    total = harga * jumlah
    total_belanja += total

    print("------------------------------------")
    print("Nama makanan    :", nama)
    print("Harga           : Rp", harga)
    print("Jumlah          :", jumlah)
    print("Total transaksi : Rp", total)
    print("------------------------------------")

# Menentukan diskon
if total_belanja > 100000:
    diskon = total_belanja * 10 / 100
else:
    diskon = 0

# Menghitung total pembayaran
total_pembayaran = total_belanja - diskon

# Menampilkan hasil
print("\n====================================")
print("          STRUK PEMBAYARAN")
print("====================================")
print("Total belanja     : Rp", total_belanja)
print("Diskon 10%        : Rp", diskon)
print("Total pembayaran : Rp", total_pembayaran)
print("====================================")
print("       TERIMA KASIH")
print("====================================")
