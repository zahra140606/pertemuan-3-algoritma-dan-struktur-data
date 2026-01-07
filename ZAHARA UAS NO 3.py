def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    jam_normal = 8
    total_gaji = 0

    for i in range(hari_kerja):
        if jam_kerja_per_hari > jam_normal:
            lembur = jam_kerja_per_hari - jam_normal
            gaji_harian = (jam_normal * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            gaji_harian = jam_kerja_per_hari * tarif_per_jam

        total_gaji += gaji_harian

    return total_gaji


# Input dari user
tarif =     int(input("Masukkan tarif gaji per jam: "))
jam_kerja = int(input("Masukkan jam kerja per hari: "))
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

# Hitung dan tampilkan gaji
total_gaji = hitung_gaji(tarif, jam_kerja, hari_kerja)
print("Total gaji bulanan: Rp", total_gaji)
