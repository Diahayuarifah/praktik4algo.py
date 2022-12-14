print("Program menampilkan jumlah hari dalam satu bulan")

import calendar
while True:
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        if bulan < 1 or bulan > 12:
            print("Bulan tidak valid")
            continue
        tahun = int(input("Masukkan tahun: "))
        print(f"Terdapat {calendar.monthrange(tahun, bulan)[1]} hari dalam bulan {bulan} tahun {tahun}")
        if input("Masukkan -1 untuk menghentikan program: ") == "-1":
            break
    except ValueError:
        print("Input tidak valid")