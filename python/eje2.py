# cada persona por promedio habla 2 palabaras por segundo,
# a) pedirle al usuario  que diga cualquier texto real y calcular cuanto tiempo tardaria en decir la frase
# b) cuantas palabras tiene la frase
# c) si tarda mas de 1 min en decir la frase, mostrar un mensaje que diga "tu frase es muy larga".
# d) si habla un 30% mas rapido, cuanto tardaria el en decir la frase

persona = 2 
frase = input("Dime una frase cualquiera:")
palabras_separadas = frase.split(" ")                    # split() --> se encarga de separar una cadena en partes, y devuelve una lista con cada parte. (por defecto, separa por espacios, pero se puede indicar otro caracter para separar).
cantidad_palabras = len(palabras_separadas)
tiempo = cantidad_palabras / 2
print(f"Tu frase tiene {cantidad_palabras} palabras y tardarias {tiempo} segundos en decirla.")
