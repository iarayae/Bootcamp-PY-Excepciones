# Bootcamp-PY-Excepciones
Desafio Bootcamp - Python - Manejo de Excepciones

## Objetivo ##

El objetivo del desafío es implementar una excepción personalizada llamada 'DimensionError', y utilizarla en la clase 'Foto' para validar que las dimensiones (alto y ancho) se mantengan dentro de los límites definidos.

## Archivos incluidos ##

- 'error.py': Contiene la definición de la excepción personalizada 'DimensionError', que hereda de 'Exception'.
- 'foto.py': Contiene la clase 'Foto', con validación en los métodos 'setter' de 'ancho' y 'alto' mediante la excepción 'DimensionError'.
- 'main.py': Archivo de prueba opcional que crea instancias de 'Foto' y muestra el comportamiento del sistema al ingresar dimensiones inválidas.

## Requisitos ##

1. Crear la excepción 'DimensionError' que reciba un mensaje, una dimensión ingresada y un valor máximo permitido.
2. Sobrecargar el método '__str__' para mostrar un mensaje claro en caso de error.
3. Modificar los métodos 'setter' de 'ancho' y 'alto' en la clase 'Foto' para que:
   - Lancen una 'DimensionError' si el valor está fuera del rango permitido (menor que 1 o mayor que 'MAX').
   - Asignen el valor normalmente si está dentro del rango.