Clave="222" "223"
 
for i in range(3):
    entrada=input("Indica la contraseña para acceder: ")
    if entrada==Clave:
        break
 
if entrada==Clave:
    print("Bienvenido al Curso de Informática I")
else:
    print("Lo sentimos, no acertaste.")