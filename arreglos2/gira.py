print("nuevo gira")
#en si la palabra tiene () caracteres pero empieza contando desde cero.
print("por favor ingrese una palabra")
palabra = input()
#palabra vale ()

nuevaPalabra = ""

for i in range( len(palabra) ):
    print( palabra[ (len(palabra) -1) -i] )
    nuevaPalabra += (palabra[ (len(palabra) -1) -i] )
    #el + con el = significa manten lo que agregaste y agrega lo nuevo
    print("la nueva palabra es: " + nuevaPalabra)

    if palabra == nuevaPalabra:
      print("la palabra :" + palabra + "es igual a la palabra" + nuevaPalabra)
    else:
     print("la palabra :" + palabra + "es diferente a la palabra" + nuevaPalabra)