abrir_menu = False
print("1. abrir menu \n")
print("2. otra cosa \n")
print("3. salir\n")

opcion_usuario = int(input())



def menu(papita):
    if papita == 1:
        print("habrio el menu")
    if papita == 2:
        print("otra cosa")
    if papita == 3:
        print("salimos")


menu(opcion_usuario)
