import matplotlib.pyplot as plt
from functools import reduce
from numpy import mean, std

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# TODO 1: Menghitung rata-rata menggunakan fungsi reduce
total_nilai = reduce(lambda x,y : x+y, nilai_mahasiswa)
rata_nilai = total_nilai / len(nilai_mahasiswa)
print("Nilai Rata-rata Mahasiswa: ",rata_nilai)

# TODO 2: Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lamda)
label_mahasiswa = list(map(lambda nilai: f"{nilai+1}", range(len(nilai_mahasiswa))))

# TODO 3: Visualisasi data dalam bentuk diagram batang
plt.figure(figsize=(8, 6))
plt.bar(label_mahasiswa, nilai_mahasiswa, color='blue')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')

plt.axhline(y=rata_nilai, color='red', linestyle='--', label=f'Rata-rata = {rata_nilai:.1f}')
plt.legend()

plt.tight_layout()
plt.show()
