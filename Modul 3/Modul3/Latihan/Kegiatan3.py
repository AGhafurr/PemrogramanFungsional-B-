random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"] 

# Filter untuk memisahkan nilai float, int, dan string
def pemisah(item): 
    if isinstance(item, int): 
        ratusan = item // 100 
        puluhan = (item % 100) // 10 
        satuan = item % 10 
        return {'int': item, 'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan} 
    elif isinstance(item, float): 
        return ('float', item) 
    elif isinstance(item, str): 
        return ('string', item) 

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
hasil_pemisahan = list(map(pemisah, random_list)) 

# Menggunakan filter() untuk memisahkan nilai int, float, dan string 
nilai_int = list(filter(lambda x: isinstance(x, dict), hasil_pemisahan)) 
nilai_float = list(filter(lambda x: isinstance(x, tuple) and x[0] == 'float', hasil_pemisahan)) 
nilai_string = list(filter(lambda x: isinstance(x, tuple) and x[0] == 'string', hasil_pemisahan)) 

# Output
print("DATA: ",random_list)
print("Data Float:", tuple([item[1] for item in nilai_float])) 
print("\nData String:", tuple([item[1] for item in nilai_string])) 
print("\nData Int:") 

for item in nilai_int:
    print({
        "Ratusan" : item["ratusan"],
        "Puluhan" : item["puluhan"],
        "Satuan" : item["satuan"]
    })

