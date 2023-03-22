import csv
import math


def read_data(fich):
    dic1 = {}
    cont = 0
    cont_lineas = 0
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
                    if i != "":
                        cont_lineas = cont_lineas + 1
                        dicaux[atributos[iterador]] = i
                    iterador = iterador + 1
                dic1["dato"+ str(cont)] = dicaux
                
            cont = cont + 1
    
    if cont_lineas < 10:
        raise ValueError("ha ocurrido la exepción ValueErrror en read_data")
    return dic1

def split(dic):
    dicRed = {}
    dicWhite = {}
    contRed = 1
    contWhite = 1
    for dato in dic:
        
        if dic[dato]["type"] == "white":
            del dic[dato]["type"]
            dicWhite["dato"+str(contWhite)] = dic[dato]
            contWhite = contWhite + 1
        elif dic[dato]["type"] == "red":
            del dic[dato]["type"]
            dicRed["dato"+str(contRed)] = dic[dato]
            contRed = contRed + 1
    return dicRed, dicWhite
    
def reduce(dic,string):
    lista = list()

    for dato in dic:
        if string in dic[dato]:
            lista.append(dic[dato][string])
        else:
            raise ValueError("ha ocurrido la excepción ValueError en reduce")
    

    return lista
def silhouette(list1,list2):
    Si = list()
    ai = list()
    bi = list()
    medai = 0.0
    medbi = 0.0
    silhouetteVal = 0.0

    for i in list1:
        for j in list1:
            if j != i:
                medai= medai + math.sqrt(math.pow(abs(i-j),2))
        medai = medai/len(list1)
        ai.append(medai)
    

    for i in list1:
        for j in list2:
            medbi= medbi + math.sqrt(math.pow(abs(i-j),2))
        medbi = medbi/len(list1)
        bi.append(medbi)

    for i in len(ai):
        Si.append((bi[i]-ai[i])/(max(ai[i],bi[i])))
    for i in Si:
        silhouetteVal = silhouetteVal + i
    silhouetteVal = silhouetteVal/len(Si)

    return silhouetteVal
    
