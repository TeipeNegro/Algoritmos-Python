#Delaramos las Variables, y les asignamos un valor mediante el input
Num_1 = int(input("Porfavor, Ingrese un Numero: "))
Num_2 = int(input("Porfavor, Ingrese Otro Numero: "))

#Si se cumple a condicional if o elif, imprimir mensaje
if Num_1 > Num_2: print(f" {Num_1} es el Mayor, {Num_2} es el Menor")
elif Num_1 == Num_2: print("Ambos Numeros Son Iguales")

#Si no se cumple ninguna de las anteriores, imprmir este mensaje
else: print(f"{Num_2} es el Mayor, {Num_1} es el Menor")

#Ejecutar por Terminal