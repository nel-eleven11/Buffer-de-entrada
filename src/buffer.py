# Actividad Práctica: Implementación de un Búfer de Entrada
# Diseño de lenguajes de programación
"""
Integrantes del grupo:
Nelson García 22434
Joaquín Puente 22296
Ricardo Chuy 22
Diego Linares 22
"""

# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
    # Procesar y extraer lexemas del buffer
    lexema = ""
    for i in range(len(buffer)):
        if buffer[i] == "eof":
            break
        elif buffer[i] == " ":
           print("Lexema procesado: " + lexema)
           lexema = ""
        else:
            lexema += buffer[i]
        
    

entrada = list("Esto es un ejemplo de entrada con eof")
inicio = 0
avance = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
print(buffer)
procesar_buffer(buffer)