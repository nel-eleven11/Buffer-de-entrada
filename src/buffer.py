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
  pass

entrada = list("Esto es un ejemplo eof")
inicio = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
procesar_buffer(buffer)