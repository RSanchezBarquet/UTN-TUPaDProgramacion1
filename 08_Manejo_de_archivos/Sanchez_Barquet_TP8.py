"""crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
with open("productos.txt", "w") as archivo:

    archivo.write("Libro,1200,4")
    archivo.write("\nLapicera,500,15")
    archivo.write("\nMarcador,1000,20")

print("archivo creado!")"""


"""Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30


with open("productos.txt", "r") as archivo:
   for linea in archivo:
       linea=linea.strip()

       datos=linea.split(",")

       nombre=datos[0]
       precio=datos[1]
       cantidad=datos[2]
       print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")"""


""" Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt", "r") as archivo:
    print("Productos actuales:\n")
    for linea in archivo:
        linea = linea.strip()
        if linea: 
            datos = linea.split(",")
            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

nuevo_producto = input("\nIngrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio del nuevo producto: ")
nueva_cantidad = input("Ingrese la cantidad del nuevo producto: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"\n{nuevo_producto},{nuevo_precio},{nueva_cantidad}")

print("Producto agregado!")"""

"""Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.

productos=[]

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
print(productos)  """

""" Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.

productos=[]

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)  
buscar_producto= input("Ingrese el nombre del producto a buscar: ")
existe= False
for producto in productos:
    if producto["nombre"] == buscar_producto:
        print(f"Producto encontrado: {producto}")
        existe = True
        break
if not existe:
    print("Producto no encontrado.")"""

"""Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista."""

productos=[]

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
buscar_producto= input("Ingrese el nombre del producto que desea buscar: ")
existe= False

for producto in productos:
    if producto["nombre"] == buscar_producto:
        print(f"Producto encontrado: {producto}")
        existe = True
        break

if not existe:
    print("el producto no existe, se agregará al archivo")    

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
print("Se actualizó el archivo de productos")



