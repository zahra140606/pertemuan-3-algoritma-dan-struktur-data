usia_input = input("Masukkan Usia (pisahkan dengan koma): ")

list_usia = [int(usia.strip()) for usia in usia_input.split(',')]

for usia in list_usia:
    if usia >= 60:
        kategori = 'Lansia'
    elif usia >= 18:
        kategori = 'Dewasa'
    elif usia >= 13:
        kategori = 'Remaja'
    elif usia >= 6:
        kategori = 'Anak anak'
    else:
        kategori = 'Balita'

    print("Usia:", usia, "-", kategori)