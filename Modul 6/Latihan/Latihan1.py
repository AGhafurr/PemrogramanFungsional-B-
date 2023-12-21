#Lengkapi kode dibawah untuk menjawab soal diatas ya

# TODO 0 : Import library lain yang dibutuhkan
from PIL import ImageDraw, ImageFont, Image


# TODO 1: Lakukan load image pada variabel berikut
gambarku = Image.open('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\Neu.jpg')


# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# # TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font_path = 'D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\ariblk.ttf'
font_size = 24
font = ImageFont.truetype(font_path, font_size)
text = "Ghafur 109"
text_width = draw.textlength(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = gambarku.height -40
draw.text((text_x, text_y), text, 225, font)


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('D:\\SEMESTER 5\\PEMROGMAN FUNGSIONAL B\\Modul\\Modul 6\\Latihan\\gambar_baru.png')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
