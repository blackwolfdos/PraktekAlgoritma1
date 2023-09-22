print("Hitung Luas Ruangan")

panjang = int(input("panjang: "))
lebar = int(input("lebar: "))
satuan = input("satuan: cm/m ")
hasil = panjang*lebar

if "cm" in satuan:
    print("luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adalah", hasil*100, "cm")
elif "m" in satuan:
    print("luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adalah", hasil,"m")