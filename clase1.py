# nombre = "pepe"

# print(f"valor: {nombre}") #que valor tiene "nombre"
# print(f"tipo: {type(nombre)}") #que tipo de dato es "nombre"
# print(f"identificador: {id(nombre)}") #asignamos un id


# UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

# Las posibles aplicaciones son las siguientes:
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA),
# Internet de las cosas (IOT)

# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# nombre del empleado
# edad (no menor a 18)
# género (Masculino - Femenino - Otro)
# tecnologia (IA, RV/RA, IOT)  
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
# Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.


nombre = input("ingresa tu nombre : ")
edad = int(input("ingrese su edad mayor a 18: "))

while True:
    if edad > 18:
        print("edad valida")
        break
    else:
        print("edad invalida")
        edad = int(input( "ingrese su edad mayor a 18  : "))

genero = input("ingresa el genero : ")
while genero != "masculino" and genero != "femenino":
    print("genero invalido")
    genero = input("ingresa el genero : ")

tecnologia = input("ingresa la tecnologia : ")
while tecnologia != "ia" and tecnologia != "rv" and tecnologia != "ra" and tecnologia != "iot":
    print("tecnologia invalida")
    tecnologia = input("ingresa la tecnologia : ")




