import functions



try:
  dic = functions.read_data('winequality.csv')
except ValueError:
  print("ha ocurrido la exepción ValueErrror en read_data")

print('-'*20 + "prueba de split" + '*'*20) 

dicRed, dicWhite = functions.split(dic)
print(dicRed,dicWhite)

print('-'*20 + "prueba de reduce" + '-'*20) 

try:
   print(functions.reduce(dicRed,"alcohol"))
except ValueError:
   print("ha ocurrido la excepción ValueError en reduce")

print('-'*20 + "prueba de silhouette" + '-'*20) 

   
list1 = functions.reduce(dicRed,"alcohol")
list2 = functions.reduce(dicWhite,"alcohol")
print(functions.silhouette(list1,list2))