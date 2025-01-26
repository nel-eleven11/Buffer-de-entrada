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
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer, avance, lexema):
    avance = 0
    
    # Procesar y extraer lexemas del buffer
    for i in range(len(buffer)):
        
        if buffer[i] == " ":
           print("Lexema procesado: " + lexema)
           lexema = ""
           print("Valor de avance: ", avance)

        elif lexema == "eof":
           print("Lexema procesado: " + lexema)
           break
           
        else:
            lexema += buffer[i]
        
        avance += 1
        
    return lexema, avance 

entrada = list("Esto es un ejemplo de entrada con eof")
inicio = 0
avance = 0

ultimo_lex = ""
tamano_buffer = 10

while ultimo_lex != "eof":

  buffer = cargar_buffer(entrada, inicio, tamano_buffer)
  print(buffer)
  ultimo_lex, avance = procesar_buffer(buffer, avance, ultimo_lex)
  inicio += avance