import csv


def read_data(fich):
    dic1 = {}
    with open(fich, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


    return dic1