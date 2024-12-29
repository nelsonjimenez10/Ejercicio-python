#Metodo count()
#cantidad de veces que un caracter o una cadena aparece dentro de un texto
#arguentos variable.count("string", posicion de inicio, posicion final)
#count incluye la posicion 0 como un caracter y suma cuando no se colocan elementos a buscar
#si se coloca un negativo en la posicion inicial se ubica de erecha a izquierda, pero el reco
#rido del metodo sigue siendo de izquierda a derecha

print("vamos a subirlo a github")
#lo que vamos a hacer es agregar esa linea de codigo para probar la rama
print("****************")
print("  metodo count  ")
print("****************")

v01=input("String: ")
v02=input("lo que busco: ")
print()
print(f"{v02} se encuentra {v01.count(v02)} veces en : {v01}")

string="mi mama me mima"
contador=0
print(string.center(40,"="))
contador=string.count("M")
print(f"n\La letra M se encontro {contador} veces en la cadena {string}")

contador=string.count("m")
print(f"n\La letra m se encontro {contador} veces en la cadena {string}")

contador=string.count("mama")
print(f"n\La letra mama se encontro {contador} veces en la cadena {string}")

contador=string.count("me mima")
print(f"n\La letra me mima se encontro {contador} veces en la cadena {string}")

contador=string.count("ma")
print(f"n\La letra ma se encontro {contador} veces en la cadena {string}")

contador=string.count("m",13)
print(f"n\La letra m se encontro {contador} veces, desde la posicion 13 en la cadena {string}")

contador=string.count("m",100)
print(f"n\La letra m se encontro {contador} veces, desde la posicion 100 en la cadena {string}")

contador=string.count("m",-3)
print(f"n\La letra m se encontro {contador} veces, desde la posicion -3 en la cadena {string}")

contador=string.count("m",3, 7)
print(f"n\La letra m se encontro {contador} veces, desde la posicion 3 hasta la 7 en la cadena {string}")

contador=string.count("m",100, 100)
print(f"n\La letra m se encontro {contador} veces, desde la posicion 100 hasta la 100 en la cadena {string}")

contador=string.count("m",-4, -1)
print(f"n\La letra m se encontro {contador} veces, desde la posicion -4 hasta la -1 en la cadena {string}")
