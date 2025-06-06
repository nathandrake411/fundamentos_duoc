

while True:
    try:
        personas = int(input("cuantas personas se van a registrar:"))
        break
    except:
        print("debe ser un numero entero")

while True:
    try:
        dosis = int(input("cuantas dosis ah recibido:"))
        if dosis >= 3:
            print("esquema completo")
        else:
            print("esquema incompleto")
        personas = +1
        break
    except:
        print("debe ingresar un numero entero")