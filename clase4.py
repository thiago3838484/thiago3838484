# def mostrar():
#     global numero
#     numero = 77
#     print(numero)

# #--------------------------------------------

# numero = 4
# mostrar()
# numero = 3
# print(numero)

#------------------------------------------------

# def contar(contador):
#     print(id(contador))
#     contador = 5
#     print(id(contador))

# contador = 10
# print(id(contador))

# contar(contador)
# print(id(contador))


# def modificar_lista(lista):
#     print(id(lista))
#     lista[2] = 1000
#     print(id(lista))

# lista = [4,9,8]
# print(id(lista))

#-------------------------------------------------
def calificar_alumno(nombre:str, presente: bool, nota1:float = None, nota2:float = None) -> bool | str:
    #calcula el promedio de notas si el alumno estuvo presente
    #nombre: nombre del alumno - presente: si estuvo presente en el examen
    #nota1: nots del primer examen, nota2: nota del segundo examen


    nota_final = "ausente"
    print(f"calificando al alumno: {nombre}")
    if presente:
        nota_final = (nota1 + nota2) / 2
    return nota_final

nota_final = calificar_alumno("juan",False,7,8)
print(nota_final)





