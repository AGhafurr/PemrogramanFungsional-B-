class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}
    
    def add_book(self, book):
        self.books.append(book)
        print(f"\"{book}\" telah ditambahkan ke perpustakaan.")

    def borrow_book(self, user, book):
        if book in self.books:
            if book not in self.borrowed_books:
                self.borrowed_books[book] = user
                print(f"{user} telah meminjam buku \"{book}\".")
            else:
                print(f"Buku \"{book}\" sudah dipinjam oleh {self.borrowed_books[book]}.")
        else:
            print(f"Buku \"{book}\" tidak tersedia di perpustakaan.")

    def return_book(self, user, book):
        if book in self.borrowed_books and self.borrowed_books[book] == user:
            del self.borrowed_books[book]
            print(f"{user} telah mengembalikan buku \"{book}\".")
        else:
            print(f"Buku \"{book}\" tidak dipinjam oleh {user}.")

def main():
    library = Library()
    
    while True:
        print("\nMenu:")
        print("1. Akun Admin - Tambah Buku")
        print("2. Akun User - Pinjam Buku")
        print("3. Akun User - Kembalikan Buku")
        print("4. Keluar")
        
        choice = input("Pilih menu (1/2/3/4): ")
        
        if choice == '1':
            if isinstance(library, Library):
                if isinstance('Admin', str):
                    book = input("Masukkan judul buku yang akan ditambahkan: ")
                    library.add_book(book)
                else:
                    print("Maaf, hanya akun admin yang dapat menambahkan buku.")
            else:
                print("Maaf, perpustakaan tidak tersedia saat ini.")
        
        elif choice == '2':
            if isinstance(library, Library):
                if isinstance('User', str):
                    book = input("Masukkan judul buku yang ingin dipinjam: ")
                    library.borrow_book('User', book)
                else:
                    print("Maaf, hanya akun user yang dapat meminjam buku.")
            else:
                print("Maaf, perpustakaan tidak tersedia saat ini.")
        
        elif choice == '3':
            if isinstance(library, Library):
                if isinstance('User', str):
                    book = input("Masukkan judul buku yang ingin dikembalikan: ")
                    library.return_book('User', book)
                else:
                    print("Maaf, hanya akun user yang dapat mengembalikan buku.")
            else:
                print("Maaf, perpustakaan tidak tersedia saat ini.")
        
        elif choice == '4':
            print("Terima kasih! Sampai jumpa lagi.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
