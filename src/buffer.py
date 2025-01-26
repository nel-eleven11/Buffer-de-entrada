# Actividad Práctica: Implementación de un Búfer de Entrada
# Diseño de lenguajes de programación
"""
Integrantes del grupo:
Nelson García 22434
Joaquín Puente 22296
Ricardo Chuy 221007
Diego Linares 22
"""


# Código base para iniciar
def cargar_buffer(entrada: list[str], inicio: int, tamano_buffer: int) -> (list[str], int):
    buffer: list[str] = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer


def procesar_buffer(lexema, buffer):
    # Procesar y extraer lexemas del buffer
    avance: int = 0
    for i in range(len(buffer)):
        avance += 1
        if buffer[i] == "eof":
            print("Lexema procesado: " + lexema)
            return None, avance
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
    parsing = True
    lexema = ""

    entrada = list("Esto es un ejemplo de entrada con eof")
    print(len(entrada))
    while parsing:
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)
        lexema, avance = procesar_buffer(lexema, buffer)
        if lexema is None:
            break

        inicio += avance


if __name__ == '__main__':
    main()
