# PROGRAM PEMBELAJARAN DASAR PYTHON
print("\n" + "="*50)
print("PENGENALAN TIPE DATA & SINTAKS DASAR PYTHON")
print("="*50 + "\n")

# ==============================================
# 1. VARIABEL DAN TIPE DATA DASAR
# ==============================================
print("[1. VARIABEL DAN TIPE DATA DASAR]")

# Integer (bilangan bulat)
umur = 20
print("Integer:", umur, type(umur))

# Float (bilangan desimal)
tinggi = 170.5
print("Float:", tinggi, type(tinggi))

# String (teks)
nama = "Budi Santoso"
print("String:", nama, type(nama))

# Boolean (True/False)
mahasiswa = True
print("Boolean:", mahasiswa, type(mahasiswa))

# NoneType (tidak ada nilai)
kosong = None
print("NoneType:", kosong, type(kosong))

print("\n" + "-"*50 + "\n")

# ==============================================
# 2. STRUKTUR KONTROL
# ==============================================
print("[2. STRUKTUR KONTROL]")

# If-Else
print("\n--- If-Else ---")
nilai = 85

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")  # Ini yang akan dieksekusi
else:
    print("Nilai C")

# Perulangan For
print("\n--- For Loop ---")
print("Perulangan list:")
for i in [1, 2, 3, 4, 5]:
    print(i, end=" ")

print("\n\nPerulangan range:")
for angka in range(3):  # 0-2
    print(angka, end=" ")

# Perulangan While
print("\n\n--- While Loop ---")
counter = 3
while counter > 0:
    print(f"{counter}...", end=" ")
    counter -= 1
print("Go!")

print("\n" + "-"*50 + "\n")

# ==============================================
# 3. STRUKTUR DATA
# ==============================================
print("[3. STRUKTUR DATA]")

# List (mutable)
print("\n--- List ---")
buah = ["Apel", "Jeruk", "Mangga"]
print("List buah:", buah)
buah.append("Anggur")
print("Setelah append:", buah)

# Tuple (immutable)
print("\n--- Tuple ---")
koordinat = (4, 5)
print("Tuple koordinat:", koordinat)

# Dictionary (key-value pair)
print("\n--- Dictionary ---")
mahasiswa = {
    "nama": "Ani",
    "nim": "123456",
    "prodi": "Teknik Informatika"
}
print("Dictionary mahasiswa:", mahasiswa)

# Set (unik & tidak berurut)
print("\n--- Set ---")
unik = {1, 2, 3, 2, 1}
print("Set angka unik:", unik)

print("\n" + "-"*50 + "\n")

# ==============================================
# 4. FUNGSI DAN KELAS
# ==============================================
print("[4. FUNGSI DAN KELAS]")

# Fungsi
print("\n--- Fungsi ---")
def sapa(nama):
    """Fungsi untuk menyapa pengguna"""
    print(f"Halo, {nama}!")

sapa("Lisa")  # Memanggil fungsi

# Kelas
print("\n--- Kelas ---")
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def meong(self):
        print(f"{self.nama}: Meong!")

kucing1 = Kucing("Tom", 2)
kucing1.meong()

print("\n" + "-"*50 + "\n")

# ==============================================
# 5. SINTAKS LAINNYA
# ==============================================
print("[5. SINTAKS LAINNYA]")

# List Comprehension
print("\n--- List Comprehension ---")
kuadrat = [x**2 for x in range(5)]
print("Kuadrat bilangan:", kuadrat)

# Try-Except
print("\n--- Try-Except ---")
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Error: Pembagian dengan nol!")

# Input Pengguna
print("\n--- Input Pengguna ---")
nama_input = input("Masukkan nama Anda: ")
print(f"Halo, {nama_input}!")

# Format String
print("\n--- Format String ---")
panjang = 5
lebar = 3
print(f"Luas persegi panjang: {panjang * lebar}")

print("\n" + "="*50)
print("Tips Belajar:")
print("- Praktekkan langsung setiap contoh")
print("- Gunakan print() untuk melihat hasil")
print("- Coba modifikasi nilai variabel")
print("- Gunakan komentar (#) untuk penjelasan")
print("="*50)
