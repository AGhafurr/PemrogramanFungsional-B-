#tuple
tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

# Buatlah sebuah fungsi untuk memisahkan data pada no.1 tersebut menjadi 2 list berdasarkan tipe datanya.
def pisah (tuple):
    nama = [tuple[i] for i in range(0, len(tuple), 2)]
    harga = [tuple[i] for i in range(1,len(tuple),2)]
    return nama, harga

# Buatlah sebuah fungsi untuk menggabungkan kedua list pada hasil no 2 menjadi sebuah dictionary berisi pasangan nama barang dan harganya.
def gabung(nama, harga):
    return dict(zip(nama, harga))
# Tampilkan hasil dari no. 1, 2, dan 3.

print("1. ", tuple)

nama, harga = pisah(tuple)
print("2. ", nama, harga)

hasil_gabung= gabung(nama, harga)
print("3. ", hasil_gabung)