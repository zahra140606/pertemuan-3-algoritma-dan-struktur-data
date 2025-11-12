nilai = int(input('Masukan nilai: '))
usia = int(input('Masukan usia: '))

if nilai >= 75:
  if (usia < 15):
    print('selamat adek, kamu lulus!')
  else:
    print('selamat kakak, kamu lulus!')
else:
  if (usia < 15):
    print('Mohon maaf dek, coba lagi ya!')
  else:
    print('Mohon maaf kak, coba lagi ya!')
    
    