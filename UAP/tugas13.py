# TODO 1: Tambahkan library yang dibutuhkan
import matplotlib.pyplot as plt
#Setiap tupel berisi informasi sebagai berikut:
#(jenis_kendaraan, penggunaan_energi_per_km, biaya_operasional_per_km)
data = [
    ('Bus', 5, 200),
    ('Trem', 8, 150),
    ('Kereta', 12, 300),
    ('Minibus', 6, 180),
    ('Tram', 9, 220)
]

# TODO 2: Pisahkan Data masing-masing (dapat menggunakan pemetaan)
jenis_kendaraan = [ elemen[0] for elemen in data]
penggunaan_energi = [ elemen[1] for elemen in data]
biaya_operasioanl = [ elemen[2] for elemen in data]

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
# TODO 3: Lengkapi kode untuk visualisasi data penggunaan energi 
plt.scatter(jenis_kendaraan, penggunaan_energi)
plt.xlabel('Jenis kendaraan')
plt.ylabel('penggunaan energi')

plt.subplot(1, 3, 2)
# TODO 4: Lengkapi kode untuk visualisasi data biaya operasional
plt.scatter(jenis_kendaraan, biaya_operasioanl)
plt.xlabel('Jenis kendaraan')
plt.ylabel('biaya operasional')

plt.subplot(1, 3, 3)
# TODO 6: Lengkapi kode untuk menggambar Scatter plot
plt.plot(jenis_kendaraan, biaya_operasioanl)
plt.xlabel('Jenis kendaraan')
plt.ylabel('biaya operasional')
# TODO 7: Memberikan label pada tiap titik

# Menambahkan legenda
plt.legend()

# Tampilkan plot
plt.tight_layout()
plt.show()