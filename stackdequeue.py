import os
from queue import LifoQueue
from collections import deque

print()
MaxSize = int(input('Masukan Jumlah data yang ingin ditambah: '))
print()
DequStack = deque()
LifoStack = LifoQueue(maxsize=MaxSize)

cek = True

while cek:
    os.system('cls')
    print('Masukan Pilihan anda:')
    print('1. Stack dengan Deque')
    print('2. Stack dengan LifoQueue')
    print('0. Keluar')
    pil = int(input('Masukan Pilihan anda: '))

    if pil == 1:
        i = 1
        os.system('cls')
        temp = True
        while temp:
            print()
            print('Masukan Pilihan anda:')
            print('1. Tambah Data dengan Deque')
            print('2. Hapus Data Deque')
            print('3. Tampil Data Deque')
            print('4. Jumlah Data Deque')
            print('0. Keluar')
            pilMenu = int(input('Masukan pilihan anda: '))
            print()

            if pilMenu == 1:
                if len(DequStack) <= MaxSize:
                    while i <= MaxSize:
                        item = input(f'Masukan data ke-{i}: ')
                        DequStack.append(item)
                        i += 1
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!!')
            elif pilMenu == 2:
                if len(DequStack) != 0:
                    print(f'Elemen terakhir: {DequStack.pop()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            elif pilMenu == 3:
                print('Data dalam Stack adalah:')
                print(DequStack)
            elif pilMenu == 4:
                print(f'Jumlah Data dalam Stack = {len(DequStack)}')
            else:
                pilMenu = False
                break

    elif pil == 2:
        os.system('cls')
        temp = True
        i = 1
        while temp:
            print()
            print('Masukan Pilihan anda:')
            print('1. Tambah Data dengan LifoQueue')
            print('2. Hapus Data LifoQueue')
            print('3. Tampil Data LifoQueue')
            print('4. Jumlah Data LifoQueue')
            print('0. Keluar')
            pilMenu = int(input('Masukan pilihan anda: '))
            print()

            if pilMenu == 1:
                if LifoStack.qsize() == 0:
                    i = 1
                if (LifoStack.qsize() + 1 <= MaxSize):
                    while i <= MaxSize:
                        item = input(f'Masukan data ke-{i}: ')
                        LifoStack.put(item)
                        i += 1
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!!')
            elif pilMenu == 2:
                if not LifoStack.empty():
                    print(f'Elemen terakhir: {LifoStack.get()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            elif pilMenu == 3:
                isi = list(LifoStack.queue)
                print('Data dalam Stack adalah:')
                print(isi)
            elif pilMenu == 4:
                print(f'Jumlah Data dalam Stack = {LifoStack.qsize()}')
            else:
                pilMenu = False
                break

    elif pil == 0:
        cek = False
        print("Keluar dari program...")
    else:
        print("Pilihan tidak ada")
