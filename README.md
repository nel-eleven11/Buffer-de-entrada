# Actividad-Buffer-de-Entrada
Pequeño simulador de un búfer de entrada en Python

---

En el código presente hay 3 funciones:

- cargar_buffer: Esta se encarga de cargar el buffer con 10 caracteres de la entrada, si los caracteres son menos que el tamaño del buffer, se hace appende del término 'eof'. Recibe como parámetros el mensaje de entrada, el tamaño del buffer y el número del lugar del primer caracter que se cargará en el buffer. Retorna el buffer cargado.

- procesar_buffer: Identifica e imprime todos los lexemas de la entrada, cada vez que detecta un espacio o el término 'eof', si alguna de esas dos condiciones no se cumple va añadiendo caracteres al lexema. También se tiene la variable avance a la cual se le suma 1 por cada caracter analizado del buffer. Se retorna el lexema en curso y el avance que se ha hecho con los caracteres de la entrada.

- main: Aquí se inicializan las variables principales, se usa el while para poder analizar todos los caracteres de la entrada, primero se carga el buffer, luego se procesa hasta que ya no haya generado ningún lexema, el avance hecho se añade a inicio para que se carge el buffer desde el siguiente caracter del último cargado anteriormente.


