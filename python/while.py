# se va ejecutar siempre y cuando la condicion sea verdadera
contador = 0
while contador < 2:
    print(f'la variable contador es: {contador}')
    contador += 1
print('el bucle ha finalizado')

print(f'---------------------------------------------------------------------------------------') 
# crear tus propias funciones 
def saludar(nombre):
    print(f'Hola {nombre} bienvenido a la programación en Python')
saludar("ignacio")


# utilizando el parametro args
def suma(*numeros):
    return sum(numeros)
resultado = suma(1,2,3,4,5,13,134,53)
print(f'la suma de los numeros es: {resultado}')

# 4.20.00
##########################################################################################################
##########################################################################################################
##########################################################################################################




