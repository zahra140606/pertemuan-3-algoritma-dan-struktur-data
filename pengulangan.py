listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 
    'Jogjakarta', 'Semarang', 'Makassar'
]
kotaYangDicari = input('ketik nama kota yang kamu cari:')

for i, kota in enumerate(listkota):
    # kita ubah katanya ke lowercase agar
    # menjadi case insesitive
    if kota.lower() == kotaYangDicari.lower():
        print('kota yang anda cari berada pada index', i)
        break
else:
    print('Maaf, kota yang anda cari tidak ada')