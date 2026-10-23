harga_sepatu = int(input("Masukkan harga sepatu: "))
jumlah_beli = int(input("Masukkan jumlah beli: "))

total = harga_sepatu * jumlah_beli

if total > 500000:
    total -= 50000

print("Total yang harus dibayar:", total)