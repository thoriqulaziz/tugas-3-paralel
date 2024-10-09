from multiprocessing import Process, Barrier

# Fungsi untuk menampilkan angka genap
def tampilkan_genap(barrier):
    for angka in range(20, 31, 2):  # Menggunakan langkah 2 untuk hanya mendapatkan angka genap
        print(f'Angka Genap: {angka}')
        # Sinkronisasi menggunakan Barrier
        barrier.wait()

def main():
    # Membuat Barrier untuk 3 proses
    barrier = Barrier(3)

    process1 = Process(target=tampilkan_genap, args=(barrier,))
    process2 = Process(target=tampilkan_genap, args=(barrier,))
    process3 = Process(target=tampilkan_genap, args=(barrier,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

if __name__ == "__main__":
    main()
