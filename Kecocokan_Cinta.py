import random
import os

def hitung_kecocokan(nama1: str, nama2: str) -> int:
    """Menghitung kecocokan cinta berdasarkan nama (deterministik)."""
    seed = sum(ord(c) for c in (nama1 + nama2).lower())
    random.seed(seed)
    return random.randint(0, 100)

def kategori_cinta(persen: int) -> str:
    """Mengembalikan kategori berdasarkan persentase kecocokan."""
    if persen >= 90:
        return "[***] Jodoh Sempurna!"
    elif persen >= 70:
        return "[** ] Sangat Cocok!"
    elif persen >= 50:
        return "[*  ] Cukup Cocok."
    elif persen >= 30:
        return "[   ] Kurang Cocok."
    else:
        return "[ x ] Tidak Cocok."

def progress_bar(persen: int, panjang: int = 20) -> str:
    """Membuat progress bar ASCII berdasarkan persentase."""
    isi = int(panjang * persen / 100)
    kosong = panjang - isi
    return "[" + "#" * isi + "-" * kosong + "]"

def clear_screen():
    """Membersihkan layar terminal (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validasi_nama(prompt: str) -> str:
    """Meminta input nama yang valid (hanya huruf dan spasi)."""
    while True:
        nama = input(prompt).strip()
        if not nama:
            print("[!] Nama tidak boleh kosong!")
        elif not all(c.isalpha() or c.isspace() for c in nama):
            print("[!] Nama hanya boleh mengandung huruf dan spasi!")
        else:
            return nama.title()

def tampil_header():
    print("=" * 40)
    print("      << KALKULATOR CINTA >>")
    print("=" * 40)

def main():
    clear_screen()
    tampil_header()

    while True:
        print()
        nama_kamu = validasi_nama("Masukkan Nama Kamu   : ")
        nama_cinta = validasi_nama("Masukkan Nama Cinta  : ")

        if nama_kamu.lower() == nama_cinta.lower():
            print("[!] Nama tidak boleh sama!")
            continue

        persen = hitung_kecocokan(nama_kamu, nama_cinta)
        status = kategori_cinta(persen)
        bar = progress_bar(persen)

        print()
        print("-" * 40)
        print(f"  {nama_kamu}  <3  {nama_cinta}")
        print(f"  Kecocokan  : {bar} {persen}%")
        print(f"  Status     : {status}")
        print("-" * 40)

        while True:
            lanjut = input("\nIngin coba lagi? (y/n) : ").strip().lower()
            if lanjut == 'y':
                clear_screen()
                tampil_header()
                break
            elif lanjut == 'n':
                print()
                print("  Terima kasih telah menggunakan Kalkulator Cinta!")
                print("=" * 40)
                return
            else:
                print("[!] Masukkan 'y' untuk ya atau 'n' untuk tidak.")

if __name__ == "__main__":
    main()
