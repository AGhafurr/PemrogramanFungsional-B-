class Buku:
    def __init__(self, judul, tersedia=True):
        self.judul = judul
        self.tersedia = tersedia

class Akun:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.pinjaman = []

    def pinjam_buku(self, buku):
        if self.jenis == "user":
            if buku.tersedia:
                buku.tersedia = False
                self.pinjaman.append(buku)
                print(f"{self.nama} telah meminjam buku '{buku.judul}'.")
            else:
                print(f"Maaf, buku '{buku.judul}' tidak tersedia saat ini.")
        else:
            print("Anda tidak memiliki izin untuk melakukan peminjaman buku.")

    def kembalikan_buku(self, buku):
        if buku in self.pinjaman:
            buku.tersedia = True
            self.pinjaman.remove(buku)
            print(f"{self.nama} telah mengembalikan buku '{buku.judul}'.")
        else:
            print(f"{self.nama} tidak memiliki buku '{buku.judul}' untuk dikembalikan.")

# Buat beberapa buku
buku1 = Buku("Harry Potter")
buku2 = Buku("To Kill a Mockingbird")
buku3 = Buku("The Great Gatsby")

# Buat akun admin dan user
admin = Akun("Admin", "admin")
user1 = Akun("User1", "user")
user2 = Akun("User2", "user")



# User1 mencoba meminjam buku
user1.pinjam_buku(buku1)
user2.pinjam_buku(buku2)

# User1 mengembalikan buku
user1.kembalikan_buku(buku1)

# User2 mencoba meminjam buku lagi
user2.pinjam_buku(buku2)

