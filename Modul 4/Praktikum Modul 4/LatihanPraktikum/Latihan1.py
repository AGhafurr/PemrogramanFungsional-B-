def perkalian(a):
    def dengan(b):
        return a*b
    return dengan

hasil_Hof = perkalian(4)
hasil_akhir_Hof = hasil_Hof(5)
print(hasil_akhir_Hof)

hasil_currying = perkalian(5)(5)
print(hasil_currying)