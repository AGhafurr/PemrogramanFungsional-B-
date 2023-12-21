from functools import reduce

Movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def Hitung_Genre(Movies):
    genres = map(lambda movie: movie["genre"], Movies)
    Genre_Hitung = reduce(lambda Hitung, genre: {**Hitung, genre: Hitung.get(genre, 0) + 1}, genres, {})
    
    return Genre_Hitung    

def Hitung_Rata_Tahun(Movies):
    tahun_rating = filter(lambda movie: movie["year"] in set(map(lambda m: m["year"], Movies)), Movies)
    Tahun_Rating = {}
    for movie in tahun_rating:
        tahun = movie["year"]
        rating = movie["rating"]
        if tahun in Tahun_Rating:
            Tahun_Rating[tahun].append(rating)
        else:
            Tahun_Rating[tahun] = [rating]

    rata_rata = {tahun: sum(ratings) / len(ratings) for tahun, ratings in Tahun_Rating.items()}
    
    return rata_rata  

def film_rating_tinggi(Movies):
    ratings = map(lambda movie: movie["rating"], Movies)
    
    highest_rating = max(ratings)
    Rating_tertinggi = filter(lambda movie: movie["rating"] == highest_rating, Movies)

    return list(Rating_tertinggi)


def Search_Movies(Movies, Movie):
    for movie in Movies:
        if movie["title"] == Movie:
            return movie

def menu():
    print("Pilih tugas yang ingin dilakukan")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")

def main():
    menu()
    while True:
        print("")
        Inputan = input("Masukkan nomor tugas: ")

        if Inputan == '1':
            hitung_genree = Hitung_Genre(Movies)
            print("Jumlah Film berdasarkan Genre")
            print(hitung_genree)

        elif Inputan == '2':
            rata_rata = Hitung_Rata_Tahun(Movies)
            print("Rata-rata Rating Film Berda1sarkan Tahun Rilis: ")    
            print(rata_rata)

        elif Inputan == '3':
            rating_tinggi = film_rating_tinggi(Movies)
            print("Film dengan Rating Tertinggi")
            print(rating_tinggi)

        elif Inputan == '4':
            Movie = input("Masukkan judul film yang ingin dicari : ")
            Search = Search_Movies(Movies, Movie)
            if Search:
                print(f"Informasi Film : {Search['title']}")
                print(f"Rating : {Search['rating']}")
                print(f"Tahun Rilis : {Search['year']}")
                print(f"Genre : {Search['genre']}")               
            else:
                print("Film dengan Judul tersebut tidak ditemukan")

        elif Inputan == '5':
            print("Terimakasih bye-byee")
            break
            
        else:
            print("Input Yang benar donggg!!!")
            print("")
            

if __name__ == "__main__":
    main()
