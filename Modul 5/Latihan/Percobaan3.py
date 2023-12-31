import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([8, 1, 12, 5])
y4 = np.array([1, 5, 10, 2])

# Membuat plot untuk garis y1 dan y2
plt.plot(y1, label='Garis 1')
plt.plot(y2, label='Garis 2')
plt.plot(y3, label='Garis 3')
plt.plot(y4, label='Garis 4', linestyle='--')

# Menambahkan judul dan label sumbu
plt.title('Plot tiga Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()
plt.show()