import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 8]
y = [3, 7, 2, 8, 5, 10]

sizes = [20, 50, 80, 200, 300, 400]  
plt.scatter(x, y, s=sizes)
plt.show()
