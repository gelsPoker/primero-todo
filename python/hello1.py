# desempaquetado las variables de la tupla
datos = ("juan","benjamin","mendoza")                       #se puede usar cualquier tipo de dato, no solo tuplas, tambien listas, diccionarios, etc
dinero = [100,200,300]
nom1,nom2,nom3 = datos
din1, din2, din3 = dinero

print(f'los nombres son: {nom1}, {nom2} y {nom3}' )
print(f'los montos son: {din1}, {din2} y {din3}')

print(f' ---------------------------------------------------------------------------------------------')
print(f' ---------------------------------------------------------------------------------------------')
print(f' ---------------------------------------------------------------------------------------------')



# creando un conjunto con set()
conjunto = set([1,2,3,4,5])
conjunto1 = set({"juan","benjamin","mendoza"})
print(conjunto)
print(conjunto1)