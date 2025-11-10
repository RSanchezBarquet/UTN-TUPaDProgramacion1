"""Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

"""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


# programa principal
nombre_usuario=input("ingresa tu nombre:")
saludar_usuario(nombre_usuario)

"""Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# programa principal
nombre_usuario=input("ingresa tu nombre: ")
apellido_usuario=input("ingresa tu apellido: ")
edad_usuario=input("ingresa tu edad: ")
residencia_usuario=input("ingresa tu residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

"""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y
 devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar
   los resultados."""

#definicion de funciones
def calcular_area_circulo(radio):
    area= 3.14*(radio**2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro=2*3.14*radio
    return perimetro

#programa principal
radio_circulo=float(input("ingresa el radio del circulo: "))

area_circulo=calcular_area_circulo(radio_circulo)
perimetro_circulo=calcular_perimetro_circulo(radio_circulo)

print(f"El area del circulo es: {round(area_circulo, 2)}")
print(f"el perimetro del circulo es: {round(perimetro_circulo, 2)}")

"""Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""


def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas

#programa principal
segundos_usuario=int(input("Ingresa los segundos: "))
cantidad_horas=segundos_a_horas(segundos_usuario)

print(f"{segundos_usuario} segundos equivalen a {round(cantidad_horas, 2)} horas.")

"""Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado=numero*i
        print(f"{numero}*{i}={resultado}")

#programa principal
numero_para_tabla=int(input("ingresa un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_para_tabla)

"""Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, 
multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

def operaciones_basicas(a, b):
    suma= a+b
    resta=a-b
    multiplicacion= a*b
    division=a/b 
    return (suma, resta, multiplicacion, division)

#programa principal
num1=int(input("ingresa el primer numero: "))
num2=int(input("ingresa el segundo numero: "))

suma, resta, multiplicacion, division=operaciones_basicas(num1, num2)

print(f"La suma de los numeros ingresados es: {suma}")
print(f"La resta de los numeros ingresados es: {resta}")
print(f"La multiplicacion de los numeros ingresados es: {multiplicacion}")
print(f"La division de los numeros ingresados es: {division}")

"""Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    return imc

#programa principal
peso=float(input("ingrese su peso em kg: "))
altura=float(input("ingrese su altura en metros:"))

imc_usuario=calcular_imc(peso, altura)

print(f"su indice de masa corporal es de : {round(imc_usuario,2)}")

"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    fahrenheit=(celsius*(9/5))+32
    return fahrenheit

#programa principal
temperatura_celsius=float(input("ingresa la temperatura en celsius: "))
temperatura_fahrenheit=celsius_a_fahrenheit(temperatura_celsius)

print(f"la temperatura {temperatura_celsius}°C equivale a {round(temperatura_fahrenheit, 2)}°F")

"""Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return promedio

#programa principal
a=float(input("ingresa el primer numero:"))
b=float(input("ingresa el segundo numero:"))
c=float(input("ingresa el tercer numero:"))

print(f"el promedio de los numeros ingresados es: {round(calcular_promedio(a, b, c), 2)}")





