def mingguu(minggu):
    def harii(hari):
        def jamm(jam):
            def menitt(menit):
                return minggu * 7 * 24 * 60 + hari * 24 * 60 + jam * 60 + jam

            return menitt

        return jamm

    return harii

data = ["3 minggu 2 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

for data_item in data:
    data_split = data_item.split()
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])
    hasil_konvers = mingguu(minggu) (hari) (jam) (menit)
    output_data.append(hasil_konvers)

print("outputData =", output_data)