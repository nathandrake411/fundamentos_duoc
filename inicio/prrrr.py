while True:
    try:
        perso_register = int(input("cuantas personas se van a registrar:"))
        break
    except:
        print("debe ser un numero entero, intente denuevo")

n = []

dosis = perso_register
n.append(perso_register)

vacunados = int(input("cuantas vacunas tiene:"))
for i in range(perso_register):
    cantidad = int(input("cuantas dosis tiene:"))
    vacunados.append(cantidad)
print(cantidad)