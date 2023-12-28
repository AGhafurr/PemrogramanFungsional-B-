def hitung_pangkat(pangkat):
    def pangkat_bilangan(bilangan):
        return bilangan ** pangkat
    return pangkat_bilangan

pangkat = hitung_pangkat(2)
hasil_pangkat_dua = pangkat(4)
print(hasil_pangkat_dua)
