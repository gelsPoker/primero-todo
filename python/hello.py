num1 = 5
num2 = 3
resul=num1/num2
print(resul)























# 2:45:00

# DATOS COMPUESTOS 
# array = [1, 2, 3, 4, 5], ["Ignacio Salazar", "Soy salto",True,1.45]  

#   ingreso = int(input("Ingrese un numero: "))
#   if ingreso > 100:
#       print("El numero es mayor a 100")
#   elif ingreso < 100:
#       print("El numero es menor a 100")
#   else:
#       print("El numero es igual a 100")


# resultado = cadena.upper()                                ------> .upper() --> Todo lo devuelve a mayuscula.
#                                                           ------> .lower() --> Convirte todo a Minuscula.
#                                                           ------> .capitalize() --> Convierte sola la primera letra a Mayuscula.

# busqueda = cadena.find("hola")                            ------> .find(" ") --> busca un caracter que le pidamos. (si no encuentra, lanza -1).
#                                                           ------> .index(" ") --> lo mismo que .find, pero si no encuentra, lanza un error.

# es_nuemrico = cadena.isnumeric()                          ------> .isnumeric() --> si es numerico, devuelve un true, sino un false.
# es_alfanumerico = cadena.isalpha()                        ------> .isalpha()   --> si es caracter, si esta separado por espacios, delvolvera false.

# contar_coincidencias = cadena.count("a")                  ------> .count()   --> devuelve la cantidad de veces que coincide.
# contar_caracteres = len(cadena1)                          ------> len()      --> contamos cuantos caracteres tiene una cadena.

#                                                           ------> .startswith("") ----> verificamos si una cadena empieza con .
#                                                           -----> .endswith("") ----->  verificamos si una cadena termina con .

#                                                           ----> .replace("hola", "hola maquina") ----> reemplaza una cadena por otra cadena.  




#                         ------------------------------METODOS DE LISTAS ------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# agregar_append = lista.append("jajaja")               ------> .append("")     --->  agregar un elemento a la lista.
#                                                       ------> .insert(2,"toma mama")  ----> agregar un elemento a la lista en el indicee indicado.
#                                                       ------> .extend([False,2030,"jal"])  ----> agregar varios elemento a la lista.

# lista.pop(0)                                          -----> .pop(0) ---> elimina un elemento de la lista, pide indice y devuelve valor.
#                                                       -----> .remove("toma mama") --> remueve un elemento de una lista, busca el valor.
#                                                       -----> .clear() --> elemina todos los elemntos de una lista.

#                                                       -----> .sort() --> los ordena ascendentemente (no pueden haver cadenas).
#                                                       -----> .reverse  --> invierte los elementos de la lista.

#                         ------------------------------METODOS DE DICCIONARIO ------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# diccionario = {
#    "nombre" : 'ignacio',
#    "apellido" : 'walter',
#   "edad" : 45,
#    "peso" : 63.4
# }
#                                                     ----> .keys() --> devuelve las claves.
# claves = diccionario.get("edad")                    ----> .get("") --> devulve el valor de una clave.
#                                                     ----> .items() --> para iterar el dict.
#
##                        ------------------------------ ENTRADAS DE DATOS ------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# nombre = input("dame tu nombre:")
#