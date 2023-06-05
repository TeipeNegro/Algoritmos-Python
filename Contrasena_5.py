intentos = 0 

while intentos < 3:
    clave = input("Porfavor, Ingrese la Clave: ")
    if clave == "352" :
        print("Clave correcta")
        intentos = 4
    else:
        print("Clave incorrecta")
        intentos += 1
        if intentos == 3:
            print("Demasiados Intentos")
