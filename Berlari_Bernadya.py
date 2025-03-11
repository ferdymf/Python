import time
from threading import Thread, Lock
import sys

lock = Lock()


def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def sing_song():
    lyrics = [
        ("\n""Aaa... tak sesuai rencana", 0.19),
        ("Aaa... bukankah harusnya", 0.19),
        ("Kita tak saling berkabar lagi", 0.23),
        ("Itu katamu kemarin...", 0.21),
        ("\n""Setidaknya aku jadi yang pertama kau kabari", 0.11),
        ("Saat harimu kurang menarik", 0.17),
        ("Sampai nanti suatu pagi", 0.10),
        ("Kau tak butuh aku lagi", 0.10),
        ("Kapan pun kau panggil", 0.12),
        ("Ku ke situ berlari", 0.19),
    ]

    delays = [0.0, 5.5, 10.4, 18.0, 24.8, 30.2, 35.5, 38.4, 40.8, 42.3]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    sing_song()
