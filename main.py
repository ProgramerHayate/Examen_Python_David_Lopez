import functions



try:
  dic = functions.read_data('winequality.csv')
except ValueError:
  print("ha ocurrido la exepción ValueErrror en read_data")
dicRed, dicWhite = functions.split(dic)
#print(dicRed,dicWhite)
try:
    print(functions.reduce(dicRed,"alcohol"))
except ValueError:
   print("ha ocurrido la excepción ValueError en reduce")