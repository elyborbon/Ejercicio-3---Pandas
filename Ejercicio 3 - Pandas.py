import pandas as pd
datos = [2,3,5,7,11]
serie = pd.Series(datos)
print (type(datos))
print (type(serie))
lista = serie.tolist()
print (type(lista))
print (type(serie))
print (lista)
