import threading


angka_awal = 43
lock = threading.Lock()

def tampilkan_angka_genap(angka):
    while angka < 100:  # Tentukan batas akhir sesuai kebutuhan
        with lock:
            if angka % 2 == 0:
                print(f"Angka Genap: {angka}")
        angka += 1  

def tampilkan_angka_ganjil(angka):
    while angka < 100:  
        with lock:
            if angka % 2 != 0:
                print(f"Angka Ganjil: {angka}")
        angka += 1  

thread_genap = threading.Thread(target=tampilkan_angka_genap, args=(angka_awal,))
thread_ganjil = threading.Thread(target=tampilkan_angka_ganjil, args=(angka_awal,))

# Menjalankan thread
thread_genap.start()
thread_ganjil.start()

# Menunggu kedua thread selesai
thread_genap.join()
thread_ganjil.join()
