# Actividad Práctica: Implementación de un Búfer de Entrada
# Diseño de lenguajes de programación
"""
Integrantes del grupo:
Nelson García 22434
Joaquín Puente 22296
Ricardo Chuy 221007
Diego Linares 221256
"""


# Se carga el buffer
def cargar_buffer(entrada: list[str], inicio: int, tamano_buffer: int) -> (list[str]):
    buffer: list[str] = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

# Procesar y extraer lexemas del buffer
def procesar_buffer(lexema, buffer):
    avance: int = 0
    for i in range(len(buffer)):
        avance += 1
        if buffer[i] == "eof":
            print("Lexema procesado: " + lexema)
            return lexema, avance
        elif buffer[i] == " ":
            print("Lexema procesado: " + lexema)
            lexema = ""
        else:
            lexema += buffer[i]

    return lexema, avance


def main():
    inicio = 0
    avance = 0
    tamano_buffer = 10
    lexema = ""

    entrada = list("Esto es un ejemplo de entrada con eof")
    print(len(entrada))

    while lexema != "eof":
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)
        lexema, avance = procesar_buffer(lexema, buffer)

        inicio += avance


if __name__ == '__main__':
    main()
