#Declaramos variable d (Dias) y le asignamos los valores (0 hasta 6) de Lunes hasta Domingo
#Por lo tanto: Lunes = 0, Martes = 1, Miercoles = 2, Jueves = 3, Viernes = 4, Sabado = 5, Domingo = 6
d = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

#Declarmos una Variable Num para asignarle un valor mediante input
num = int(input("Porfavor, Ingrese un Numero: "))

#Si se cumple la condicional, dentro del rango determinado, entonces imprimir la variable d en base a la variable num -1
#Caso contrario, imprimir mensaje else
if (num >=1) and (num <= 7): print(d[num-1])
else: print("El Numero que Ingreso no es Valido")

#Ejecutar por Terminal