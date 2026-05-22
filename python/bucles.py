# iterar listas
animales = ["Perro","Gato","Pájaro","María","pez"]
for animal in animales:
    print(f'la vaaariable animal es: {animal}')
print(f'---------------------------------------------------------------------------------------')   

numeros = [1,2,3,4,5]
for numero in numeros:
    numeros = numero * 10
    print(f'la variable numero multiplicada por 10 es: {numeros}')
print(f'---------------------------------------------------------------------------------------')  

# iterar con la funcio range
for i in range(5,10):
    print(f'la variable i es: {i}')
print(f'---------------------------------------------------------------------------------------')  

# forma de recorrer uns lista con su indice
for indice, animal in enumerate(animales):
    print(f'el animal en el indice {indice} es: {animal}')

# todo lo anterior funciona con cualquier tipo de dato, no solo con listas, tambien con tuplas, diccionarios, etc.

print(f'---------------------------------------------------------------------------------------') 
# usando el for/else
# el else se ejecutara siempre
for numeros in range(3):
    print(f'la variable numero es: {numeros}')
else:
    print('el bucle ha finalizado')


print(f'---------------------------------------------------------------------------------------') 
# recorriendo un diccionario
diccionario = {
    "nombre": "ignaciO",
    "apellido": "salazar",
    "edad": 30,
    "prof": True
} 
for key in diccionario:              # al momento de poner key, nos muestra la clave.
    print(key)
for key in diccionario.items():      # al momento de poner items, nos muestra la clave y el valor.
    print(key)
