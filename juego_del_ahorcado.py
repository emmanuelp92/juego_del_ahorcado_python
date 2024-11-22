
import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "javascript",
        "java",
        "angular",
        "django",
        "tensorflow",
        "react",
        "typescrpt",
        "git",
        "flask",
    ]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"

    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡BIenvenido al juego del ahorcado!")
    print(f"Tenés {intentos} intentos para daviniar la palabra secreta.")
    print(
        mostrar_progreso(palabra_secreta, letras_adivinadas),
        "La cantidad de letras de la plabra secreta es:",
        len(palabra_secreta),
    )

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor, introduce solo letras.")
        elif adivinanza in letras_adivinadas:
            print("Ya utilizaste esa letra, introduce otra.")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print("¡Muy bien! Econtraste una letra.")
            else:
                intentos -= 1
                print(
                    f"La letra '{adivinanza}' no está en la palabra secreta. Ingresa otra."
                )
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(
                f"¡Felicitaciones has ganado! La plalabra secreta es: '{palabra_secreta}'"
            )

    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Se te acabaron los intentos, la palabra secreta era: {palabra_secreta}")


juego_ahorcado()
