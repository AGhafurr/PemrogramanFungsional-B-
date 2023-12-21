import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10, 9])
ypoints = np.array([3, 10, 8, 15])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color='blue')
plt.xlim([0,23])
plt.ylim([0,22])
plt.xlabel('Titik X')
plt.ylabel('titikY')
plt.title('Percobaan 2')
plt.show()