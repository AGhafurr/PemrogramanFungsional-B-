#Lengkapi kode dibawah ini untuk menjawab soal diatas ya


# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw

# TODO 1 : Buka kedua gambar menggunakan Pillow.
background_image = Image.open('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Praktikum\\BG.jpeg')
overlay_image =  Image.open('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Praktikum\\LOGO.jpeg')


# TODO 2 : Ubah gambar background menjadi hitam-putih (grayscale), berotasi sebesar 30 derajat, dan blur
gambarBW = background_image.convert("L")
rotatedImage = gambarBW.rotate(30)
blurred_image = rotatedImage.filter(ImageFilter.BLUR)

# TODO 3 : Ubah tingkat kecerahan gambar overlay menjadi 1.x kali lipat dan tingkat kontras
# menjadi 1.y kali lipat. Dimana nilai x dan y mengacu pada 2 digit NIM akhir kalian
# dan resize sesuai kebutuhan.

#tingkat brightness menjadi 1.09
enhancer = ImageEnhance.Brightness(blurred_image)
brightened_img = enhancer.enhance(1.09)  

#tingkat kontras menjadi 1.09
enhancer = ImageEnhance.Contrast(brightened_img)
final_img = enhancer.enhance(1.09) 


# TODO 4: Sisipkan gambar overlay ke dalam gambar background sehingga terlihat seperti stiker pada gambar latar belakang.
# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (final_img.width - overlay_image.width) // 2
y_center = (final_img.height - overlay_image.height) // 2

final_img.paste(overlay_image, (x_center, y_center))

# TODO 4 : Tambahkan teks "Informatika JOSSS!" pada gambar overlay dengan font Arial dan ukuran 24
draw = ImageDraw.Draw(final_img)
font_path = 'D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\ariblk.ttf'
font_size = 24
font = ImageFont.truetype(font_path, font_size)
text = "Informatika JOSSS!"
text_width = draw.textlength(text, font)
text_x = 30
text_y = 30
draw.text((text_x, text_y), text, 255, font)

# TODO 5 : Simpan gambar hasil edit dengan nama "tugas_praktikum_enam.jpg".
final_img.save('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Praktikum\\tugas_praktikum_enam.png')

# TODO 6 : Tampilkan
final_img.show()
