
    #hacer un codigo que identifique si una palabra es palindromo o no
print("----- imprimir todas las letras de una palabra -----")
nuevaPalabra = "ana"

for i in range(len(nuevaPalabra)):
    print(nuevaPalabra[i])

    # Verificar si es palíndromo

palabra = input("Ingresa una palabra: ").strip().lower()

# Invertir la palabra
invertida = palabra[::-1]

# Mostrar cada letra (opcional)
print("\nLetras de la palabra:")
for letra in palabra:
    print(letra)

# Comprobar y mostrar resultado
if palabra == invertida:
    print(f"\n'{palabra}' es un palíndromo.")
else:
    print(f"\n'{palabra}' NO es un palíndromo.")

    
