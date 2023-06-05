#Declaramos las Variables
contrasena = int(0)
intentos = int(0)

#Si se cumple el true, imprimir mensaje e ingresar contraseña por input
while True: 
    contrasena = int(input("Porfavor, Ingrese a Contraseña: ")) 

    #Contador de intentos
    intentos = intentos + 1

    #Si se comple la condicion, contador = 3, imprimir mensaje
    if contrasena == 352 or contrasena == 259 or contrasena == 569 or intentos == 3:
        if intentos == 3:
            print("Lo Sentimos, Demasiados Intentos")

        #Caso contrario, contraseña correcta, imprmir mensaje
        elif contrasena == 352 or contrasena == 259 or contrasena == 569:
            print("La Contraseña es Coreccta")

            break