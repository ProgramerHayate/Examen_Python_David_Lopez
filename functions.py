import csv


def read_data(fich):
    dic1 = {}
    cont = 0
    atributos = list()
    with open(fich, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if cont == 0:
                atributos = row
            else:
                dicaux = {}
                iterador = 0
                for i in row:
                    
                    dicaux[atributos[iterador]] = i
                dic1["dato"+ str(cont)] = dicaux
            cont = cont + 1
    print(dic1["dato1"])

    return dic1