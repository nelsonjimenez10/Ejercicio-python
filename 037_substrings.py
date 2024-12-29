#substrings
#       variable[inicio:final:saltos] todos enteros, inicio y final
#pueden ser positivos o negativos

# la verdad no recuerdo exacteament muchos comados de python

string="0123456789"
substring=""
print(f"Cadena principal {string}\n ")
substring=string[0]
print(f"Subcadena con indice en la posicion 0 es : {substring}\n ")
substring=string[5]
print(f"Subcadena con indice en la posicion 5 es : {substring}\n ")
substring=string[-4]
print(f"Subcadena con indice en la posicion -4 es : {substring}\n ")
substring=string[0:3]
print(f"Subcadena con indices en la posicion [0:3] es : {substring}\n ")
substring=string[:3]
print(f"Subcadena con indices en la posicion [:3] es : {substring}\n ")
substring=string[5:]
print(f"Subcadena con indices en la posicion [5:] es : {substring}\n ")
substring=string[-4:-1]
print(f"Subcadena con indices en la posicion [-4:-1] es : {substring}\n ")
substring=string[:]
print(f"Subcadena con indices en la posicion [:] es : {substring}\n ")
substring=string[1:6:2]
print(f"Subcadena con indices en la posiciones y salto [1:6:2] es : {substring}\n ")
substring=string[::3]
print(f"Subcadena con indices en la posiciones y salto [::3] es : {substring}\n ")
