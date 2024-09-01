#1. LONGITUD DE UNA FRASE.

while True:  # Se inicia un bucle que se repetirá hasta que se ingrese una palabra válida.
    palabra = input("Ingresa una palabra (solo letras): ")  # Se solicita al usuario que ingrese una palabra.

    # Se verifica si la palabra contiene solo letras.
    if palabra.isalpha():  # Con este método, comprobamos si la palabra ingresada contiene solo letras.
        longitud = len(palabra)  # Se calcula la longitud de la palabra.

        if longitud < 4:  # Se verifica si la longitud es menor que 4 letras.
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")  # Se imprime un mensaje en caso que faltan letras.
        elif longitud > 8:  # Se verifica si la longitud es mayor que 8 letras.
            print(f"Sobran letras. Tiene {longitud} letras.")  # Se imprime un mensaje en caso que sobrem letras.
        else:  # Si la longitud está entre 4 y 8 letras (inclusive).
            print("La palabra es correcta.")  # Se imprime si la palabra es correcta.
        break  # Sale del bucle porque la palabra es válida.
    else:  # Si la palabra contiene números u otros caracteres no permitidos.
        print("La entrada contiene números o caracteres no permitidos. Intenta de nuevo.")  # Se solicita al usuario que intente de nuevo.

#################################################################################################################################################################################

# 2. ENCUENTRA EL CUADRANTE.

# Solicitar y validar la coordenada X.
while True:  # Este es un Bucle infinito que solo se detiene si se recibe una entrada válida.
    valor_x = input("Ingrese X: ").strip()  # Se solicita al usuario la entrada de la coordenada X y elimina espacios en blanco al principio y al final.
    # Se verifica si la entrada es un número entero (positivo o negativo).
    if valor_x.isdigit():
        x = int(valor_x)  # Convierte el valor a entero.
        break  # Sale del bucle si la entrada es válida.
    else:
        print("Entrada inválida. Por favor, ingrese un número entero.")  # Mensaje de error si la entrada no es válida.

# Solicitar y validar la coordenada Y.
while True:  # Este es un Bucle infinito que solo se detiene si se recibe una entrada válida.
    valor_y = input("Ingrese Y: ").strip()  # Se solicita al usuario la entrada de la coordenada Y y elimina espacios en blanco al principio y al final.
    # Se verifica si la entrada es un número entero (positivo o negativo).
    if valor_y.isdigit():
        y = int(valor_y)  # Convierte el valor a entero.
        break  # Sale del bucle si la entrada es válida.
    else:
        print("Entrada inválida. Por favor, ingrese un número entero.")  # Mensaje de error si la entrada no es válida.

# Se verifica que las coordenadas no sean 0.
if x == 0 or y == 0:  # Si alguna de las coordenadas es 0.
    print("Las coordenadas no deben ser 0.")  # Mensaje de error si alguna coordenada es 0.
else:
    # Se determina en qué cuadrante se encuentra el punto.
    if x > 0 and y > 0:  # Si ambas coordenadas son positivas.
        print("El punto se encuentra en el cuadrante I")  # El punto está en el primer cuadrante.
    elif x < 0 and y > 0:  # Si la coordenada X es negativa y la coordenada Y es positiva.
        print("El punto se encuentra en el cuadrante II")  # El punto está en el segundo cuadrante.
    elif x < 0 and y < 0:  # Si ambas coordenadas son negativas.
        print("El punto se encuentra en el cuadrante III")  # El punto está en el tercer cuadrante.
    elif x > 0 and y < 0:  # Si la coordenada X es positiva y la coordenada Y es negativa.
        print("El punto se encuentra en el cuadrante IV")  # El punto está en el cuarto cuadrante.