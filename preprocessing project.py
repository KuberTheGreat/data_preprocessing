import csv

data = []

with open('dwarf_stars.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        data.append(row)

headers = data[0]

star_data = data[1:]

for data_points in star_data:
    data_points[2] = data_points[2].lower()

star_data.sort(key = lambda star_data: star_data[2])

with open('dwarf_stars_sorted.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

dataset1 = []
dataset2 = []

with open('bright_stars.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset1.append(row)

with open('dwarf_stars_sorted.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]

star_data1 = dataset1[1:]
star_data2 = dataset2[1:]

headers = header1 + header2

star_data = []

for index, data_row in enumerate(star_data1):
    star_data.append(star_data1[index] + star_data2[index])

with open('star_final.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)