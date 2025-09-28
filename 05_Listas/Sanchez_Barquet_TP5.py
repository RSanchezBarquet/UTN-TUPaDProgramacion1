"""Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja."""
notasEstudiantes=[]

for i in range(10):
    nota=float(input(f"ingres la nota del estudiante {i+1}: "))
    notasEstudiantes.append(nota)

print("nota de los estudiantes:", notasEstudiantes)#mostramos las notas de los estudiantes

promedio= sum(notasEstudiantes)/len(notasEstudiantes)

print(f"el promedio de las notas de los estudiantes es: {promedio}")

maximaNota= max(notasEstudiantes)
minimaNota= min(notasEstudiantes)

print(f"La máxima nota registrada es: {maximaNota}")
print(f"La mínima nota registrada es: {minimaNota}")

"""2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista."""

listadoProductos=[]

for i in range(5):
    producto=input(f"ingrese el producto {i+1}: ")
    listadoProductos.append(producto)

print("Lista de productos en orden alfabetico:")
print(sorted(listadoProductos))

eliminarProducto=input("Qué producto desea eliminar de la lista? ")

if eliminarProducto in listadoProductos:
    listadoProductos.remove(eliminarProducto)
    print(f"el producto: {eliminarProducto} se sacó de la lista")
else:
        print("el producto no se encuentra en la lista")

print("la lista actualizada es la siguiente:")
print(sorted(listadoProductos))


"""Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista."""


import random

nrosAzar= [random.randint(1,100) for i in range(15)]
print("lista de quince numeros al azar: ", nrosAzar)

nrosPares=[]
nrosImpares=[]

for numero in nrosAzar:
    if numero%2==0:
        nrosPares.append(numero)
    else:
        nrosImpares.append(numero)

print(f"lista de numeros pares: {nrosPares}")
print(f"lista de numeros impares: {nrosImpares}")

print("total de numeros pares: ", len(nrosPares))
print("Total de numeros impares", len(nrosImpares))

"""Dada una lista con valores repetidos:
datos=[1,3,5,3,7,1,9,5,3]
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado."""

datos=[1,3,5,3,7,1,9,5,3]

sinRepetidos=list(set(datos))

print("la lista sin datos repetidos queda de la siguiente manera: ", sinRepetidos)

"""Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada."""

presentes=[]

for i in range(8):
    estudiamte=input(f"ingrese el estudiante presente {i+1}: ")
    presentes.append(estudiamte)

print("Lista de estudiantes presentes en orden alfabetico:")
print(sorted(presentes))

eliminarEstudiante=input("Qué estudiante desea sacar de la lista? ")

if eliminarEstudiante in presentes:
    presentes.remove(eliminarEstudiante)
    print(f"el estudiante: {eliminarEstudiante} se sacó de la lista")
else:
        print("el estudiante no se encuentra en la lista")

agregarEstudiante=input("Desea agregar un estudiante? S para sí, N para no ")

if agregarEstudiante.lower()== "S" or "s":
     nuevoEstudiante=input("ingrese el nombre del nuevo estudiante: ")
     if nuevoEstudiante not in presentes:
          presentes.append(nuevoEstudiante)
          print(f"el estudiante {nuevoEstudiante} se agregó a la lista")
else:
     print("el estudiante ya está en la lista")

print("la lista de estudiantes actualizada es la siguiente:")
print(sorted(presentes))

"""Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero)."""
numeros = [5,6,7,8,9,10,11]

ultimo = numeros[-1]  # selecciono el último
resto = numeros[:-1] # selecciono todos menos el último
rotada = [ultimo] + resto # armo lista nueva
#muestro resultado
print("Lista original:", numeros)
print("Lista rotada: ", rotada)


"""Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica"""

#creo matriz con temperaturas por día (min y max)de ejemplo
temperaturas = [
    [12, 20],  
    [13, 22],  
    [11, 20],  
    [16, 25],  
    [14, 26],  
    [15, 28],  
    [18, 27]   
]

# realizo suma para luego sacar promedios
suma_min = sum([fila[0] for fila in temperaturas])
suma_max = sum([fila[1] for fila in temperaturas])

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print(f"El promedio de las temperaturas mínimas registradas es: {promedio_min:.2f}°C")
print(f"El promedio de las temperaturas máximas registradas es: {promedio_max:.2f}°C")

# Calculo amplitud térmica por día (máx - mín)
amplitud = [fila[1] - fila[0] for fila in temperaturas]

# calculo día con mayor amplitud
mayor_amplitud = max(amplitud)
dia_mayor_amplitud = amplitud.index(mayor_amplitud) + 1

print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C en el día {dia_mayor_amplitud}.")


"""Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia."""

#matriz con las notas de 5 estudiantes(fila) en 3 materias(columna)

notas = [
    [2,4,8],  
    [8,9,6],   
    [5,7,9],  
    [10,9,8],   
    [8,6,10]    
]

#promedio de estudiante
print("Promedio de cada estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio_est = sum(fila) / len(fila)
    print(f"El promedio del estudiante {i}: {promedio_est:.2f}")

#promedio por materia
print("El promedio de cada materia es:")
num_estudiantes = len(notas)
num_materias = len(notas[0])

for j in range(num_materias):
    suma_materia = 0
    for i in range(num_estudiantes):
        suma_materia += notas[i][j]
    promedio_mat = suma_materia / num_estudiantes
    print(f"Materia {j+1}: {promedio_mat:.2f}")


"""Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada."""


#inicializar tablero 3x3
tablero = [["-" for _ in range(3)] for _ in range(3)]

#definimos funcion que muestra tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()


jugadores = ["X", "O"]
turno = 0  # 0 = jugador X, 1 = jugador O

for i in range(9): # se puede jugar 9 turnos
    mostrar_tablero(tablero)
    
    jugador = jugadores[turno]
    print(f"Es turno del jugador {jugador}")
    
    # iniciamos ciclo para ver posicion valida
    while True:
        fila = int(input("Ingrese fila (0-2): "))
        col = int(input("Ingrese columna (0-2): "))
        if 0 <= fila <= 2 and 0 <= col <= 2 and tablero[fila][col] == "-":
            tablero[fila][col] = jugador
            break
        else:
            print("Posición inválida. Probá de nuevo. ")
    
    turno = 1 - turno  #cambio de turno

mostrar_tablero(tablero)
print("Juego terminado.")


"""Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana"""

#matriz de 4(productos) por 7(dias)
ventas = [
    [2,3,4,6,5,8,7],  
    [8,7,9,4,1,6,5],     
    [13,14,15,16,10,18,11]
    [2,8,7,9,5,3,7]      
]

num_productos = len(ventas)
num_dias = len(ventas[0])

#Total de ventas por producto
print("Total vendido por cada producto:")
totales_productos = []
for i, fila in enumerate(ventas):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

#día con más ventas
totales_dias = []
for j in range(num_dias):
    total_dia = sum(ventas[i][j] for i in range(num_productos))
    totales_dias.append(total_dia)

dia_mayor = totales_dias.index(max(totales_dias)) + 1
print(f"Día con mayor cantidad de ventas: Día {dia_mayor} con {totales_dias[dia_mayor-1]} ventas")

#producto que más se vendió en la semana
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} con {max(totales_productos)} unidades")
