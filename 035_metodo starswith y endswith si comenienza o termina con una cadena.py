# Metodos para determinar si una cadena comienza o termina con una
#subcadena en particular

#starswich() si inicia con una cadena en particular en un rango
#dentro de la cadena

#           variable.starswith("string", inicio, longitud de cadena)
#string="Diana se peina sola"
#string.starswith("Diana")
#logica: evalua la longitud de la subcadena en esta caso 5,
#evalua en la cadena principal que en 5 caracteres coincida la subcadena
#entrega verdadero o falso, en este ejemplo el resultado es verdadero

#endswith() si TERMINA con una cadena en particular en un rango
#dentro de la cadena

#           variable.starswith("string", inicio, longitud de cadena)
#string="Diana se peina sola"
#string.starswith("sola")
#logica: evalua la longitud de la subcadena en esta caso 4,
#luego a partir del final se  enla posicion -4
#luego compara de izquierda a derecha que coincidan cadena y subcadena
#entrega verdadero o falso, en este ejemplo el resultado es verdadero
#al colocar el rango completo tomara el rango final como referente
#tambien podemos colocar el intervalo en negativos

string="Diana se peina sola"
resultado=0
star_swith="Ejemplos con starswith():"
end_swith="Ejemplos con endwith: "

print(f"\n{star_swith.rjust(50, '=')} ")

resultado=string.startswith("D")
print(f"\n{string} comienza con la subcadena D:  {resultado}")

resultado=string.startswith("d")
print(f"\n{string} comienza con la subcadena d:  {resultado}")

resultado=string.startswith("Diana")
print(f"\n{string} comienza con la subcadena Diana:  {resultado}")

resultado=string.startswith("se", 6)
print(f"\n{string} comienza con la subcadena se, desde la posicion 6:  {resultado}")

resultado=string.startswith("se", 6,7)
print(f"\n{string} comienza con la subcadena se, desde la posicion 6 hasta la posicion 7:  {resultado}")

resultado=string.startswith("se", 100,100)
print(f"\n{string} comienza con la subcadena se, desde la posicion 100 hasta la posicion 100:  {resultado}")

resultado=string.startswith("se", -4,-1)
print(f"\n{string} comienza con la subcadena se, desde la posicion -4 hasta la posicion -1:  {resultado}")



print(f"\n{end_swith.rjust(50, '=')} ")

resultado=string.endswith("A")
print(f"\n{string} termina con la subcadena A:  {resultado}")

resultado=string.endswith("a")
print(f"\n{string} termina con la subcadena a:  {resultado}")

resultado=string.endswith("sola")
print(f"\n{string} termina con la subcadena sola:  {resultado}")

resultado=string.endswith("sola", 10)
print(f"\n{string} termina con la subcadena sola, dsde la posiscion 10:  {resultado}")

resultado=string.endswith("s", 9, 14)
print(f"\n{string} termina con la subcadena s, dsde la posiscion 9 hast ala posision 14:  {resultado}")

resultado=string.endswith("s", 100, 100)
print(f"\n{string} termina con la subcadena s, dsde la posiscion 100 hast ala posision 100:  {resultado}")

resultado=string.endswith("s", -4, -2)
print(f"\n{string} termina con la subcadena s, dsde la posiscion -4 hast ala posision -2:  {resultado}")





