# iterar listas
animales = ["Perro","Gato","Pájaro","María","pez"]
for animal in animales:
    print(f'la vaaariable animal es: {animal}')
print(f'---------------------------------------------------------------------------------------')   

numeros = [1,2,3,4,5]
for numero in numeros:
    numeros = numero * 10
    print(f'la variable numero multiplicada por 10 es: {numeros}')
print(f'-----------------------------')  

# iterar con la funcio range
for i in range(5,10):
    print(f'la variable i es: {i}')
print(f'-----------------------------')  

# forma de recorrer uns lista con su indice
for indice, animal in enumerate(animales):

# todo lo anterior funciona con cualquier tipo de dato, no solo con listas, tambien con tuplas, diccionarios, etc.

# iterar conjuntos v