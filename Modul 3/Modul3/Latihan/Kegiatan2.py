
data = ["3 minggu 2 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

for data_item in data:
    data_split = data_item.split()
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])


    nilai_integer = list(filter(str.isdigit, data_split))
    print(nilai_integer)
    output_data.append(nilai_integer)

# print("outputData =", output_data)