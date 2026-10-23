# Input
nama_buku = input("Masukkan nama buku: ")
harga = int(input("Masukkan harga buku: "))

# Proses dan output
if harga > 150000:
    print("\nBuku:", nama_buku)
    print("Anda mendapatkan Sampul Plastik Gratis")
else:
    print("\nBuku:", nama_buku)
    print("Terima kasih sudah membeli")
