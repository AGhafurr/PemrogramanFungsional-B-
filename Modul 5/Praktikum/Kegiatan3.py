import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10 

# TODO 1: buat Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def hitung_frekuensi(tinggi_badan, interval):
    interval_count = {}
    for tinggi in tinggi_badan:
        i = tinggi // interval * interval
        interval_count[i] = interval_count.get(i, 0) + 1
    return interval_count

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
frekuensi = hitung_frekuensi(tinggi_badan, interval_size)

# TODO 3: Visualisasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins=range(150, 190 + interval_size, interval_size), label= "Data")
plt.xlabel('Interval Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Frekuensi Tinggi Badan')

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
mean = np.mean(tinggi_badan)
std_dev = np.std(tinggi_badan)
x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
pdf = norm.pdf(x, mean, std_dev)
plt.plot(x, pdf * len(tinggi_badan) * interval_size, label="PDF (Normal Distribution)", color="Red")

plt.legend()
plt.show()