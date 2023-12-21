import matplotlib.pyplot as plt

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
x = [data[1] for data in data_transaksi]
y = [data[2] for data in data_transaksi]

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(13, 5))

plt.subplot(121)  
plt.scatter(x, y)
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')

# TODO 3: Hitung total pendapatan untuk setiap produk
total_pendapatan = [data[1] * data[2] for data in data_transaksi]

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
label_Produk = [data[0] for data in data_transaksi]
plt.subplot(122)
plt.bar(label_Produk, total_pendapatan)
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan Produk')
plt.title('Pendapatan Produk')

plt.tight_layout()
plt.show()

# PS: Kalian bisa memanfaatkan list comprehension, map, dan lambda
# contoh output: (bebas divariasikan sesuai selera)
