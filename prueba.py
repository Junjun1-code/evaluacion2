# Evaluacion2 13-05-25 / Nicolás Aguilar

#Pedir genero, promedio de notas y ingresarlas en listas independientes entre si
notas=[]
genero=[]
for i in range(500):
    notas.append(float(input(f"Ingresar nota del estudiante {i+1}: ")))
    genero.append(input("Ingresar genero M/F: "))

# Se usa la funcion [count] para contar cuantas mujeres existen en el registro
print(f"La cantidad de mujeres en el estudio son: {genero.count("F")}")


# Se cuentan y registran las notas. Unicamente realizando el proceso en caso de ser un hombre
cont=0
total=0
for i in range(500):
    if genero[i]=="M":
        total+=notas[i]
        cont+=1

# Se muestra el promedio que tuvieron los varones, usando la suma de sus notas y dividiendolos por su cantidad. Se reduce a 2 decimales
print(f"El promedio de notas de los varones es {total/cont:.2f}")



# Se cuentan las notas que superan 5.5
cont=0
for i in notas:
    if i>5.5:
        cont+=1
#Se muestra al usuario cuantas notas superaron 5.5
print(f"{cont} estudiantes sacaron una nota superior a 5.5")

# Se usa la funcion [min] para sacar la nota más baja
print(f"La nota más baja fue {min(notas)}")

# Se usa la funcion [max] para sacar la nota más alta, y además se usa index para encontrar la ubicación del valor más alto
print(f"La nota más alta es {max(notas)} y esta la tiene el estudiante {notas.index(max(notas))+1}")