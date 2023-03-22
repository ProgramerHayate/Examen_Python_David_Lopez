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
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
print(functions.silhouette(list1,list2))