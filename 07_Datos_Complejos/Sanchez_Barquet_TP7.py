""" Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""

precio_frutas= {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precio_frutas["Naranja"]=1200
precio_frutas["Manzana"]=1500
precio_frutas["Pera"]=2300

print(precio_frutas)

"""Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precio_frutas={'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precio_frutas["Banana"]=1330
precio_frutas["Manzana"]=1700
precio_frutas["Melón"]=2800

print(precio_frutas)

"""Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios."""


precio_frutas={'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200,
                'Manzana': 1700, 'Pera': 2300}

lista_frutas= list(precio_frutas.keys())
print(lista_frutas)

"""Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""


contactos={}

for i in range(5):
    nombre=input("ingrese el nombre del contacto: ")
    numero_tel=int(input("ingrese el numero del contacto: "))
    contactos[nombre]=numero_tel
    print(contactos)

    buscar_contacto=input("escribi el nombre el contacto que deseas buscar: ")

    if buscar_contacto in contactos:
        print(f"El numero de {buscar_contacto} es {contactos[buscar_contacto]}")
    else:
        print("El contacto no está agendado")
    

"""Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

frase=input("ingrese una frase: ")
palabras_unicas=set(frase.split())
print(f"Palabras unicas: {palabras_unicas}")

cont_palabras={}

for palabra in frase.split():
    if palabra in cont_palabras:
        cont_palabras[palabra]+=1

    else:
        cont_palabras[palabra]=1

print(f"Recuento: {cont_palabras}")

"""Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""


alumnos={}

for i in range(3):
    nombre=input("ingrese el nombre del alumno: ")
    notas=()
    for j in range(3):
        nota=float(input(f"ingrese la nota {j+1} del alumno {nombre}: "))
        notas+= (nota,)

    alumnos[nombre]=notas

print(f"Alumnos:{alumnos}")

for nombre, notas in alumnos.items():
    promedio=sum(notas)/3
    print(f"El promedio de las notas del alumno {nombre} es: {round(promedio, 2)}")

""" Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""

parcial1={"Antonio", "Carlos", "Romina"}
parcial2={"Carlos", "Melisa", "Julieta"}

ambos_aprobados= parcial1 & parcial2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_aprobados}")

uno_aprobado= parcial1 ^ parcial2
print(f"Estudiantes que solo aprobaron un parcial: {uno_aprobado}")

al_menos_uno_aprobado= parcial1| parcial2
print(f"Estudiantes que aprobaron al menos uno de los parciales: {al_menos_uno_aprobado}")

"""Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""


stock_productos={"carpeta":40, "cartucheras":24, "Marcadores":30}
producto=input("ingrese el producto del que desea consultar el stock: ")

if producto in stock_productos:
    print(f"el producto {producto} cuenta con un stock de {stock_productos[producto]} unidades")
    agregar_unidades=int(input(f"ingrese la cantidad de unidades que desea agregar al producto {producto}: "))
    stock_productos[producto]+= agregar_unidades
    print(f"el producto {producto} se actualizo a un stock de {stock_productos[producto]} unidades")

else:
    nuevo_producto= input("El producto no existe, ingrese el nombre para agregarlo al stock: ")
    stock_nuevo_producto=int(input(f"ingrese la cantidad de unidades del nuevo producto {nuevo_producto}: "))
    stock_productos[nuevo_producto]= stock_nuevo_producto

print(f"Stock actualizado: {stock_productos}")


"""Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora."""


agenda={}

for i in range(2):
    dia=input("ingrese el dia del evento en formato dd/mm: ")
    hora=input("ingrese la hora del evento en formato hh:mm: ")
    evento=input("ingrese el nombre del evento: ")
    agenda[dia, hora]= evento

print("Agenda:")
for clave, valor in agenda.items():
    print(f"{clave}: {valor}")

consulta_dia=input("ingrese el dia para consultar: ")
consulta_hora=input("ingrese la hora que desea consultar: ")

if (consulta_dia, consulta_hora) in agenda:
    print(f"Se encontró el evento: {agenda[consulta_dia, consulta_hora]} para esa fecha y hora")
else:
    print("no hay eventos programados para esa fecha y hora")
    
    
""" Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores."""


paises_capitales={"Argentina":"Buenos Aires", "Uruguay":"Montevideo", "Bolivia":"Sucre"}

capitales_paises={}

for pais, capital in paises_capitales.items():
    capitales_paises[capital]=pais
   

print(capitales_paises)





