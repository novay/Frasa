import csv
import os

file_csv = 'data/nama-gender-combined.csv'

def get_nama():
    list_nama = read_csv()

    nama_cowok = list()
    nama_cewek = list()

    for i in list_nama:
        counts = list_nama[i]
        tuple = (i, counts[0], counts[1])
        if counts[0] > counts[1]:
            nama_cowok.append(tuple)
        elif counts[1] > counts[0]:
            nama_cewek.append(tuple)

    nama = (nama_cowok, nama_cewek)
    return nama

def read_csv():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path) + '/'

    nama = dict()
    with open(dir_path + '/' + file_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            nama[row['nama']] = [int(row['m']), int(row['f'])]
    return nama