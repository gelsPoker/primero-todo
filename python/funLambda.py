# creando una funcion lambda que multiplica por 2
multiplicar = lambda x : x * 2
print(multiplicar(51))

# creand0 una funcion que me diga si es par.
num = [1,2,3,4,5,6,7,8,9,10]
def es_par(num):
    if (num%2 == 0):
        return True
    else:
        return False
print(f'la variable es par: {es_par(10)}')
print(es_par(7))

# haciendo lo mismo con una funcion lambda
numeros_pares = filter(lambda num: num%2 == 0, num)
print(f'la variable numeros pares es: {list(numeros_pares)}')
print(f'---------------------------------------------------------------------------------------')






# ejericicios practicos 2 (falto el profesor)
# 1 alumno es el profesor, 1 alumno el asistente 
# a) pedirle la edad de los compañeros que vinieron a clase y ordenar los datos de menor a mayor
# b) El mayor es el profesor y el menor es el asistente. ¿Quien es quien?

def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input(f'INGRESE SU NOMBRE:')
        edad = int(input(f'INGRESE SU EDAD:'))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x: x[1])                  # Ordenar por edad
    asistente = compañeros[0][0]                         # El menor es el asistente   
    profesor = compañeros[-1][0]                         # El mayor es el profesor
    return asistente, profesor

asistente, profesor = obtener_compañeros(3)
print(f'El profesor es: {profesor} y su asistente es: {asistente}')

