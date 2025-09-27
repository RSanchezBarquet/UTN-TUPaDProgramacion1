"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea"""
for i in range (101): #ponemos 101 para que tenga en cuenta el 100
    print(i)

"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
#pedimos al usuario que ingrese un numero entero
numero = int(input("Ingresa un número entero: "))

numero_abs = abs(numero)#convertimos a positivo

# pasamos el numero a cadena para contar los digitos
cantidad_digitos = len(str(numero_abs))

print("El número tiene", cantidad_digitos, "dígito(s).")#mostramos resultado


"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

#pedimos al usuario que ingrese dos numeros enteros
nroInicial = int(input("Ingresa el primer número entero: "))
nroFinal = int(input("Ingresa el segundo número entero: "))

# Determinamos cuál es el menor y el mayor
menor = min(nroInicial, nroFinal)
mayor = max(nroInicial, nroFinal)

# sumamos los valores excluyendo los ingresados
suma = 0
for i in range(menor + 1, mayor):
    suma += i

print("La suma de los números entre", menor, "y", mayor, "es:", suma)#mostramos resultado


"""Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

sumaTotal= 0#iniciamos en 0 para almacenar la suma de los nros ingresados
numero = int(input("ingrese un numero (0 para cortar) "))#pedimos al usuario que ingrese un numero

#ciclo while para que se repita hasta que el usuario ingrese 0
while numero != 0:
    sumaTotal += numero#sumamos al/a los nros ingresados
    numero = int(input("ingrese otro numero (0 para cortar) "))

print ("la suma de los numeros ingresados es: " , sumaTotal)#resultado

"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

nroSecreto= random.randint(0,9) #generamos numero aleatorio entre 0 y 9

intentos = 0 #iniciamos la variable en 0 para almacenar la cantidad de intentos
aleatorio = -1#iniciamos variable que almacenera el nro ingresado por el usuario. -1 para que arranque con un nro distinto al secreto antes de entrar al ciclo

print ("Bienvenido/a! Adiviná un número entre 0 y 9 : ")

while aleatorio != nroSecreto :
    aleatorio=int(input("Ingresá un numero entre 0 y 9: "))#pedimos al usuario que adivine un nro entre 0 y 9#
    intentos +=1 #sumamos la cantidad de intentos
    if aleatorio<nroSecreto:
        print("Intenta con un numero mayor")# si el nro es menor que el secreto pedimos al usuario que pruebe con un nro mayor
    elif aleatorio>nroSecreto:
        print("Intenta con un numero menor")# si el nro es mayor que el secreto pedimos al usuario que pruebe con un nro menor

#mostramos resultado
print(f"Adivinaste!!! El numero es:  {nroSecreto}" )
print(f"Adivinaste en {intentos} intentos")

"""Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for i in range (100, -1, -2):#Recorrido del 100 al 0 inlcusive en orden decreciente de 2 en 2
    print(i) #mostramos resultado

"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

numero=int(input("ingrese un numero entero positivo: "))#pedimos al usuario que ingrese un nro entero positivo

suma = 0#iniciamos la variable que almacenará la suma entre 0 y nro ingresado por usuario

for i in range (numero):#recorremos nros del 0 al ingresado sin incluirlo. si deseamos incluirlo -->for i in range(numero +1)
    suma+=i #sumamos cada nro ingresado al total
#mostramos resultado:
print(f"la suma de los numeros entre 0 y tu numero ingresado: {numero} es: {suma}")

"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

nrosIngresados=100 #establecemos la cantidad de nros que solicitaremos al usuario

#iniciamos variables para almacenar la cantidad de cada una
pares=0
impares=0
negativos=0
positivos=0

for i in range(nrosIngresados):#recorremos del 0 hasta el nro ingresado en el orden 100
    numero=int(input(f"ingrese el numero {i+1} : "))# pedimos que ingrese el numero1 , luego el numero 2...hasta pedir el nro 100

    if numero %2 ==0:
        pares +=1   #Contamos numeros pares, usamos el modulo, ya que todo numero divisible por 2 es par
    else:
        impares+=1 #contamos impares, usamos else por si no se cumple la condicion anterior de nro par

    if numero>0:
        positivos+=1 #contamos nros positivos(mayores a 0)
    elif numero<0:
        negativos+=1 #contamos nros negativos(menores a 0)

#mostramos el resultado
print("Numeros pares ingresados: ", pares)
print("Numeros impares ingresados: ", impares)
print("Numeros positivos ingresados: ", positivos)
print("Numeros negativos ingresados: ", negativos)


"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

nrosIngresados=100 #establecemos la cantidad de nros que pediremos al usuario

suma=0 #iniciamos la variable en 0 que almacenará la suma de los nros ingresados

for i in range(nrosIngresados):#recorrido de los nros ingresados 
    numero=int(input(f"Ingrese el numero {i+1} : "))# pedimos al usuario que ingrese los numeros
    suma+=numero #sumamos los nros que se van ingresando

media= suma/nrosIngresados #calculamos el promedio, es decir la media

#mostramos el resultado
print(f"la media de los numeros ingresados es: {media}")

"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""
#pedimos al usuario que ingrese un numero
numero= int(input("ingresa un numero: "))

invertido=0 #iniciamos la variable que almacenará el nro invertido
#iniciamos ciclo
while numero>0:
    digito=numero%10 #acá obtenemos el ultimo digito.
    invertido= invertido*10 + digito #agregamos al invertido. 
    numero= numero//10 #eliminamos el ultimo digito.
#mostramos el resultado
print("el numero invertido del numero ingresado es: ", invertido)