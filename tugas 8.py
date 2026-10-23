harga_beli = int(input("Masukkan harga beli: "))
harga_jual = int(input("Masukkan harga jual: "))

selisih = harga_jual - harga_beli

if harga_jual > harga_beli:
    print("Untung sebesar", selisih)
else:
    print("Rugi")