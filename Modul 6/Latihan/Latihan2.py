#Lengkapi kode dibawah ini untuk menjawab soal diatas ya


# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\NeuBackground.jpg')
overlay_image =  Image.open('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\Neu.jpg')


# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert('RGB')


# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
new_size = (500, 300)
resized_image = background_image.resize(new_size)


# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2


# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))
# resized_image.paste(overlay_image, (x_center, y_center))
# TODO 5 : Simpan gambar hasil edit
background_image.save('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\hasil_gabungan.png')

# TODO 6 : Tampilkan
background_image.show()
