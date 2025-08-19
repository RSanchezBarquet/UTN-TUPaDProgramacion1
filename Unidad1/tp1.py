"""Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""
print("Hola mundo")

"""Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""

nombre= input("¿cómo te llamas?")
print(f"Hola {nombre}!")

"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""

nombre=input("Ingresa tu nombre:")
apellido=input("Ingresa tu apellido:")
edad= input("ingresa tu edad:")
lugar= input("Ingresa tu país:")

print(f"Soy{nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

"""Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""
from cmath import pi
radio=float(input("ingrese el radio del circulo:"))
area=round(pi*radio*radio,2)
perimetro=round(2*pi*radio,2)

print(f"El area del circulo es {area} y su perimetro es {perimetro}")


"""Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""

segundos=float(input("ingrese la cantidad de segundos:"))
horas=round(segundos/3600,2)

print(f"la cantidad de {segundos} segundos equivale a {horas} horas")

"""Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número"""

numero=int(input("ingrese el numero para elaborar la tabla de multiplicar:"))

numx1= numero*1
numx2=numero*2
numx3= numero*3
numx4=numero*4
numx5= numero*5
numx6=numero*6
numx7= numero*7
numx8=numero*8
numx9= numero*9
numx10=numero*10

print (f"""a continunacion puede visualizar la tabla del numero {numero}:
       {numero} x 1= {numx1}
       {numero} x 3= {numx3}
       {numero} x 4= {numx4}
       {numero} x 5= {numx5}
       {numero} x 7= {numx7}
       {numero} x 8= {numx8}
       {numero} x 9= {numx9}
       {numero} x 10= {numx10}""")

"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""

num1= int(input("ingresa el primer nro entero distinto a 0:"))
num2=int(input("ingresa otro nro entero distinto a 0:"))
suma=num1+num2
resta=num1-num2
division=round(num1/num2,2)
multiplicacion=num1*num2

print(f"""la suma de los nros ingresados es: {suma},
         el resultado de la resta de los nros ingresados es {resta}
        la multiplicacion de los nros ingresados es: {multiplicacion}
        la division de los nros ingresados es {division}""")

"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. """   

altura=float(input("Ingrese su altura:"))    
peso=float(input("ingrese su peso:"))   
imc=peso/(altura*altura)  

print(f"su imc es {imc}")

""" Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit"""

celsius=float(input("ingrese la temperatura en celsius:"))
fahrenheit=(celsius*9)/5+32
print(f"la temperatura {celsius} grados celsius equivale a {fahrenheit} grados fahrenheit")

"""Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""
num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
num3= int(input("ingrese el tercer numero:"))
promedio=(num1+num2+num3)/3

print(f"el promedio de los numeros ingresados es: {promedio}")