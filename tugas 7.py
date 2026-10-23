nama = input("Masukkan nama siswa: ")
rata = int(input("Masukkan rata-rata nilai: "))
kehadiran = int(input("Masukkan jumlah kehadiran: "))

if rata > 70 and kehadiran > 80:
    print(nama, "Naik Kelas")
else:
    print(nama, "Tinggal Kelas")