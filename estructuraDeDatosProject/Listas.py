#Listas
from traceback import print_tb

lista = [ ]#Definir una lista vacia
print(lista)
lista1 = [1,2,3,4,5,"Hola", 4.5] #Lista heterogenea
print(lista1)
#Enlasar las listas
lista2 = [0,1,2,3]
lista3 = ["A","B","C"]
lista4 = [lista2,lista3]
print(lista4)
print(lista4[1][1])