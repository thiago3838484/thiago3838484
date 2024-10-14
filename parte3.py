# Una empresa se dedica a la venta y distribución de equipos electrónicos en el país. Dispone de
# 10 sucursales en diferentes ciudades, cada una equipada para manejar distintos tipos de
# productos.
# Las sucursales pueden almacenar 3 categorías de productos: notebooks, smartphones y
# tablets. Los precios de los mismos están expresados en dólares, según la siguiente tabla:
# La oficina central recibe un informe sobre el inventario actual en cada sucursal, que incluye el
# stock de cada categoría de producto.
# Necesitamos un programa que permita realizar la carga del inventario (realizada a mano con
# una carga secuencial en donde el stock de cada producto deberá estar validado entre 50 y
# 500 unidades). Luego realizar un menú que en cada opción resuelva los siguientes
# requerimientos:
# 2
# Producto Precio en USD
# notebook 999
# smartphone 1499
# tablet 799
# 1. Calcular el inventario total (stock disponible) de cada sucursal .
# 2. Promedio de unidades de cada producto entre todos los depósitos.
# 3. Determinar el nombre de el/los productos con más stock de cada sucursal.
# 4. El o los productos con mayor existencias en dólares entre todos los depósitos.
# 5. Crear un informe detallado con las unidades disponibles por sucursal, ordenadas de
# forma ascendente.


nombres_productos = ["notebook", "smartphone", "tablet"]
precios = [999,1499,799]

matriz = [ [128, 355, 422], [367, 105, 256], [482, 203, 379], [150, 477, 320], [291, 167, 401], [354,
232, 488], [59, 275, 182], [420, 384, 121], [219, 499, 305], [136, 411, 267] ]

inventario = [[0] * 3 for _ in range(10)] 

def cargar_inventario(matriz):
    for i in range(10):
        print(f"ingrese el stock para la sucursal {i + 1}: ")
        for j in range(3):
            while True:
                stock = int(input(f"ingrese el stock de {nombres_productos[i]} (50-500): "))
                if 50 <= stock <= 500:
                    inventario[i][j] = stock
                    break
                else:
                    print("error, el stock debee estar entre 50 y 500 unidades")




#1. Calcular el inventario total (stock disponible) de cada sucursal .

def calcular_inventario_total(matriz):
    totales = [0] * len(matriz)
    for i in range(len(matriz)):
        total = 0
        for cantidad in matriz[i]:
            total += cantidad
        totales[i] = total
    return totales

#2. Promedio de unidades de cada producto entre todos los depósitos.

def promedio_unidades(matriz):
    total_productos = [0,0,0]
    for producto in matriz:
        for i in range(3):
            total_productos[i] += producto[i]
    promedio = [0] * 3
    for i in range(3):
        promedio[i] = total_productos[i] // len(matriz)
    return promedio

#3. Determinar el nombre de el/los productos con más stock de cada sucursal.

def productos_con_mas_stock(matriz):
    maximo_stock = [0] * len(matriz)
    for i in range(len(matriz)):
        for cantidad in matriz[i]:
            if cantidad > maximo_stock:
                maximo_stock[i] = cantidad
    
    maximos = [[] for _ in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(3):
            if inventario[i][j] == maximo_stock[i]:
                maximos[i] += [nombres_productos]
    return maximos

def producto_con_mayor_existencias_dolares(inventario):
    existencias_dolares = [0] * 3

    for sucursal in inventario:
        for i in range(3):
            existencias_dolares[i] += precios[i] * sucursal[i]
    maximas_existencias = 0
    for cantidad in existencias_dolares:
        if cantidad > maximas_existencias:
            maximas_existencias = cantidad

    productos_maximos = []
    for i in range(len(existencias_dolares)):
        if existencias_dolares[i] == maximas_existencias:
            productos_maximos += [nombres_productos[i]]
    return productos_maximos

def informe_detallado(inventario):
    totales_por_sucursal = [0] * len(inventario)
    for i in range(len(inventario)):
        total = 0
        for cantidad in inventario[i]:
            total += cantidad
        totales_por_sucursal[i] = total

    for i in range(len(totales_por_sucursal)):
        for j in range(i+1, len(totales_por_sucursal)):
            if totales_por_sucursal[i] > totales_por_sucursal[j] = totales_por_sucursal[j]
    

    





# mayor_producto = producto_con_mayor_existencias_dolares(inventario)
# print(f"el producto con mayor existencia en dolares es: {mayor_producto}")
# carga = cargar_inventario(matriz)
# resultado = calcular_inventario_total(matriz)
# print(f"el calculo total es: {resultado}")
# promedio = promedio_unidades(matriz)
# print(f"el promedio es: {promedio}")
# maximo = productos_con_mas_stock(matriz)
# print(f"el producto con mas stock es: {maximo}")

