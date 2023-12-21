class Perpustakaan:
  def __init__(self): 
     self.buku = [ "Bumi","The Star and I","Harry Potter"]
     self.Peminjaman_buku = {}

  def tambah_buku(self, book):
    self.buku.append(book)
    print(f"\"{book}\"sudah di input ke program perpustkaan")   

  def Pinjam_buku(self, user, book):
    if book in self.buku:
      if book not in self.Peminjaman_buku:
        self.Peminjaman_buku[book] = user
        print(f"\"{book}\" telah dipinjam oleh {user}")
      else:
          print(f"Buku \"{book}\" sudah tidak tersedia")

  def pengembalian_buku(self, user, book):
      if book in self.Peminjaman_buku and self.Peminjaman_buku[book] == user:
          del self.Peminjaman_buku[book]
          print(f"Buku \"{book}\" telah dikembalikan oleh {user}")
      else:
          print(f"Buku \"{book}\" tidak dipinjam oleh {user}.")    

  def list_buku(self):
     if self.buku:
        print("List Buku yang tersedia: ")
        for book in self.buku:
           print(f"- {book}")
     else:
        print("Perpustakaan dalam keadaan kosong")

def login_user():
     username = input("Masukkan username User: ")  
     passw = input("Masukkan Pasword User: ") 
     return username == "User" and passw == "USR"

def login_admin():
   username1 = input("Masukkan username User: ")  
   passw1 = input("Masukkan Pasword User: ") 
   return username1 == "Admin" and passw1 == "ADM"

def main():
    perpus = Perpustakaan()
    
    while True:
      print("\n Selamat Datang di GH Library")
      print("1. Akun Admin - Tambah Buku")
      print("2. Akun User - Pinjam Buku")
      print("3. Akun User - Kembalikan Buku")
      print("4. Keluar")

      inputan = input("Pilihan anda: ")

      if inputan == '1':
         if login_admin():
             if isinstance('Admin', str):
               book = input("Inputkan Judul Buku: ")
               perpus.tambah_buku(book)     
         else:
            print("MOHON MAAF ADA KESALAHAN")

      elif inputan == '2':
         if login_user():
            perpus.list_buku()
            if isinstance('User', str):
               book = input("inputkan judul buku yang anda inginkan: ")
               perpus.Pinjam_buku('User', book)
            else:
               print("Mohon maaf, hanya User yang bisa melakukan peminjaman pada perpustakaan ini")
         else:
            print("MOHON MAAF ADA KESALAHAN")
            
      elif inputan == '3':
          if isinstance('User', str):
             book = input("Judul buku yang ingin anda kembalikan: ")
             perpus.pengembalian_buku('User', book)
          else:
             print("Mohon maaf, hanya User yang bisa melakukan pengembalian buku pada perpustakaan ini")
         
      elif inputan == '4':
            print("Terimakasih sudah mengunjungi GH Library! See you next time")
            break
      else:
            print("Silahkan pilih dengan benar!!!")

if __name__ == "__main__":
  main()    