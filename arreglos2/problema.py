lista_de_usuario = []

def ingresar_usuario(nombre_usuario):
    lista_de_usuario.append(nombre_usuario)
def eliminar_usuario(nombre_usuario):
    lista_de_usuario.remove(nombre_usuario)
def buscar_usuario(nombre_usuario):
    for i in lista_de_usuario:
        if(i == nombre_usuario):
            break
        else:
            return False
        return True

ingresar_usuario("juanito")
ingresar_usuario("maria")
ingresar_usuario("ana")
ingresar_usuario("pepito")

eliminar_usuario("ana")