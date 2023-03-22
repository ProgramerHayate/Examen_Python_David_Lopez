import functions


dic = functions.read_data('winequality.csv')

dicRed, dicWhite = functions.split(dic)
#print(dicRed,dicWhite)
print(functions.reduce(dicRed,"alcohol"))