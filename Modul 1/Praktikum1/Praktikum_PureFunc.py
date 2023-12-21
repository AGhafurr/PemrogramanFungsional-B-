def tambah_buku(books, book):
    books.append(book)
    print(f"\"{book}\"sudah di input ke program perpustkaan")   

def Pinjam_buku(books, user, book, Peminjaman_buku):
    if book in books:
      if book not in Peminjaman_buku:
        Peminjaman_buku[book] = user
        print(f"\"{book}\" telah dipinjam oleh {user}")
      else:
          print(f"Buku \"{book}\" sudah tidak tersedia")

def pengembalian_buku(user, book, Peminjaman_buku):
    if book in Peminjaman_buku and Peminjaman_buku[book] == user:
        del Peminjaman_buku[book]
        print(f"Buku \"{book}\" telah dikembalikan oleh {user}")
    else:
        print(f"Buku \"{book}\" tidak dipinjam oleh {user}.")    

def list_buku(books):
    if books:
        print("List Buku yang tersedia: ")
        for book in books:
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
    books = ["Bumi", "The Star and I", "Harry Potter"]
    Peminjaman_buku = {}
    
    
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
               tambah_buku(books, book)     
         else:
            print("MOHON MAAF ADA KESALAHAN")

      elif inputan == '2':
         if login_user():
            list_buku(books)
            if isinstance('User', str):
               book = input("inputkan judul buku yang anda inginkan: ")
               Pinjam_buku(books, 'User', book, Peminjaman_buku)
            else:
               print("Mohon maaf, hanya User yang bisa melakukan peminjaman pada perpustakaan ini")
         else:
            print("MOHON MAAF ADA KESALAHAN")
            
      elif inputan == '3':
          if isinstance('User', str):
             book = input("Judul buku yang ingin anda kembalikan: ")
             pengembalian_buku('User', book, Peminjaman_buku)
          else:
             print("Mohon maaf, hanya User yang bisa melakukan pengembalian buku pada perpustakaan ini")
         
      elif inputan == '4':
            print("Terimakasih sudah mengunjungi GH Library! See you next time")
            break
      else:
            print("Silahkan pilih dengan benar!!!")

if __name__ == "__main__":
  main()    