# Evaluacion2 13-05-25 / Nicolás Aguilar

#Pedir genero, promedio de notas y ingresarlas en listas independientes entre si
notas=[]
genero=[]
total=0
cont_nota=0
for i in range(500):
    notas.append(float(input(f"Ingresar nota del estudiante {i+1}: ")))
    genero.append(input("Ingresar genero M/F: "))
    if genero[i]=="M":
        total+=notas[i]
        # Se agrega para calcular el promedio en el futuro UNICAMENTE si es un hombre
    if notas[i]>5.5:
        cont_nota+=1
        # Se contabiliza la nota en caso de haber superado la nota 5.5 para mostrarla después en el codigo

# Se usa la funcion [count] para contar cuantas mujeres existen en el registro
print(f"La cantidad de mujeres en el estudio son: {genero.count("F")}")

# Se muestra el promedio que tuvieron los varones, usando la suma de sus notas y dividiendolos por su cantidad. Se reduce a 2 decimales
print(f"El promedio de notas de los varones es {total/genero.count("M"):.2f}")
        
#Se muestra al usuario cuantas notas superaron 5.5
print(f"{cont_nota} estudiantes sacaron una nota superior a 5.5")

# Se usa la funcion [min] para sacar la nota más baja
print(f"La nota más baja fue {min(notas)}")

# Se usa la funcion [max] para sacar la nota más alta, y además se usa index para encontrar la ubicación del valor más alto
print(f"La nota más alta es {max(notas)} y esta la tiene el estudiante {notas.index(max(notas))+1}")