abrir_menu = False
abrir_mochila = False

def menu(abrir_mochila):

    global abrir_menu
    
    if opcion == 1:
        abrir_menu = True
        print("menu abierto")
        print("1.pokedex")
        print("2.equipo")
        print("3.mochila")
        print("4.guardar")
        print("5.volver")

        opcion_dentro_del_menu = int(input("ingrese el numero"))
        if opcion == 3:
            mochila(True)
    if opcion == 2:
        abrir_menu = False
        print("menu cerrado")

def mochila(abrir_mochila):
    if abrir_mochila == True:
        print()
    else:
        print()




print("bienbenido al menu")
print("1. abrir menu")
print("2. cerrar menu")
opcion = int(input())
menu(opcion)