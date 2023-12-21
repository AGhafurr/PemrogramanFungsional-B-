import math

def point(x, y):
    return x, y

def line_equation_of(p1, M):
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

def translasi(func):
    def transformasi(p):
        x, y = p
        x_baru, y_baru = func(p)
        return (x + x_baru, y + y_baru)
    return transformasi

def rotasi(func):
    def transformasi(p):
        x, y = p
        x_baru, y_baru = func(p)
        return (x * x_baru - y * y_baru, x * y_baru + y * x_baru)
    return transformasi

def dilatasi(func):
    def transformasi(p):
        x, y = p
        x_baru, y_baru = func(p)
        return (x * x_baru, y * y_baru)
    return transformasi

x = int(input("Masukkan koordinat X: "))
y = int(input("Masukkan koordinat Y: "))
gradien = int(input("Masukkan nilai Gradient: "))
sudut = float(input("Masukkan sudut rotasi dalam derajat: "))
tx = float(input("Masukkan titik translasi X: "))
ty = float(input("Masukkan titik translasi Y: "))
sx = float(input("Masukkan faktor skala pada sumbu X: "))
sy = float(input("Masukkan faktor skala pada sumbu Y: "))

#persamaan pertama
xy = x,y
print(f"Persamaan garis yang melalui satu titik {xy} dan bergradien {gradien}:")
titik_P = point(x, y)
print(line_equation_of(titik_P, gradien))

# Dekorator transformasi
@translasi
def translasi_func(p):
    return tx, ty

@rotasi
def rotasi_func(p):
    sudut_radian = math.radians(sudut)
    return math.cos(sudut_radian), math.sin(sudut_radian)

@dilatasi
def dilatasi_func(p):
    return sx, sy

# Transformasi titik
titik_setelah_translasi = translasi_func(titik_P)
print(titik_setelah_translasi)
titik_setelah_rotasi = rotasi_func(titik_setelah_translasi)
print(titik_setelah_rotasi)
titik_setelah_dilatasi = dilatasi_func(titik_setelah_rotasi)
print(titik_setelah_dilatasi)

#persamaan garis setelah ditransformasi
persamaan_setelah_transformasi = line_equation_of(titik_setelah_dilatasi, gradien)
print("Persamaan garis setelah transformasi: ")
print(f"{persamaan_setelah_transformasi}")