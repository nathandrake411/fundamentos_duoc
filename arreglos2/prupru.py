lista_users = []

def insertar_user(nombre_user):
    print(nombre_user)







def iniciar_programa(opcion):
    while True:
        if opcion == 1:
            insertar_user()
            break
        if opcion == 2:
            buscar(usuario)
        if opcion == 3:
            eliminar_user(usuario)

opcion = int(input("ingrese opcion"))
usuario = input