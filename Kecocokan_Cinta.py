import random

print('----[Kecocokan Cinta]----')
while True:
    input_nama = input('Masukkan Nama Kamu : ')
    if input_nama.isalpha():
        input_cinta = input('Masukkan Cinta Kamu : ')
        if input_cinta.isalpha():
            cinta = random.randint(0, 100)
            print(
                f'[+] Cinta antara {input_nama} dan {input_cinta} Sebesar {cinta}%')
        lanjut = input(f'Apakah Ingin Coba Lagi? (y/n) : ')
        if lanjut == 'y':
            continue
        elif lanjut == 'n':
            print('Terima Kasih')
            break
        else:
            print('[!] Masukkan Nama Cintamu Dengan Benar!')
    else:
        print('[!] Masukkan Nama Kamu Dengan Benar!')
