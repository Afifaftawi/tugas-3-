def segitiga_penuh(tinggi):
    for i in range(tinggi):
        print(' ' * (tinggi - i - 1) + '*' * (2 * i + 1))

tinggi = int(input("Masukkan tinggi segitiga penuh: "))
segitiga_penuh(tinggi)
