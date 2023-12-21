from PIL import ImageEnhance, Image

# Buka gambar menggunakan Pillow
img = Image.open('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\Neu.jpg')

# Ubah tingkat kecerahan dan kontras
enhancer = ImageEnhance.Brightness(img)
brightened_img = enhancer.enhance(1.5)  

#tingkat kontras menjadi 1.2 
enhancer = ImageEnhance.Contrast(brightened_img)
final_img = enhancer.enhance(1.2) 

# Simpan gambar hasil edit dengan nama "brightness_contrast_image.jpg"
final_img.save('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\brightness_contrast_image.jpg')

# Tampilkan hasilnya
final_img.show()

