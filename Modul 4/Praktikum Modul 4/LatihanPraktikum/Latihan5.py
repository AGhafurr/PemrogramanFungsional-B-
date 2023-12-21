def point(x, y): 
    return x, y 
 
def line_equation_of(p1, p2): 
    # Menghitung nilai gradien (m) 
    delta_y = p2[1] - p1[1] 
    delta_x = p2[0] - p1[0] 
 
    # Mencegah pembagian dengan nol 
    if delta_x == 0: 
        raise ValueError("Titik p1 dan p2 memiliki koordinat x yang sama. Garis vertikal tidak memiliki gradien.") 
 
    M = delta_y / delta_x 
 
    # Menghitung nilai konstanta (c) menggunakan titik p1 
    C = p1[1] - M * p1[0] 
 
    return f"y = {M:.2f}x + {C:.2f}" 
 
# Mengganti nilai input dengan 4 digit NIM akhir (ganjil) 
print("Persamaan garis yang melalui titik A dan B:") 
print(line_equation_of(point(1, -1), point(0, 9)))