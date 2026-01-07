def hitung(a, b, op):
    if op == "1": return a + b
    if op == "2": return a - b
    if op == "3": return a * b
    if op == "4": return "Error: Pembagian dengan nol tidak diperbolehkan" if b == 0 else a / b
    return "Pilihan tidak valid"

print("""Pilih operasi:
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian""")

op = input("Masukkan pilihan (1/2/3/4): ")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("Hasil:", hitung(a, b, op))