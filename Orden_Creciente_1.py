#Declaramos Variables, y asignamos valores mediante input
Num_1 = int(input("Porfavor, Ingrese el Primer Numero: "))
Num_2 = int(input("Porfavor, Ingrese el Segundo Numero: "))
Num_3 = int(input("Porfavor, Ingrese el Tercer Numero: "))

#Si se cumplen las condicionales, mostrar mensaje
if Num_1 < Num_2 < Num_3: print(f"Los Numeros {Num_1} {Num_2} y {Num_3} Estan en Orden Creciente")
elif Num_1 > Num_2 > Num_3: print(f"Los Numeros {Num_1} {Num_2} y {Num_3} Estan en Orden Decreciente")
else: print("Los Numeros no estan en Orden Creciente ni Decreciente")

#Ejecutar por Teminal