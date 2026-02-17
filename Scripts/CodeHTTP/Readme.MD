### *Este script lee un archivo CSV que contiene una columna llamada "URL" y verifica cuáles enlaces funcionan correctamente (es decir, devuelven código HTTP "200").*

#
# Ventajas:
  -Usa múltiples hilos (ejecución en paralelo).

  -Tiene sistema de reintentos automáticos si una página responde con error temporal.

# Al finalizar:

  -Guarda únicamente las filas cuya URL respondió correctamente.

  -Divide los resultados en varios archivos si son muchos.

  -Muestra en consola qué URLs fueron válidas.

# En resumen: Limpia tu base de datos dejando solo URLs que realmente funcionan.


## Dependencias

Necesitas instalar: *pandas & requests*

  Usa el siguiente comando:
    -pip install pandas
    -pip install requests


## Librerías utilizadas:
  -pandas → leer y guardar CSV
  -requests → hacer solicitudes HTTP
  -concurrent.futures → ejecutar en paralelo
  -urllib3 → manejar reintentos automáticos



## Cómo usarlo:

  -Coloca tu archivo "Base_de_datos.csv" en la misma carpeta.

  -ASEGURATE de que tenga una columna llamada "URL".

Ejecuta:

  python Codigos_HTTP.py


Se generarán archivos como:

  -output_ok_code_200_part_1.csv
  -output_ok_code_200_part_2.csv
    
      **Cada uno contiene solo URLs válidas.**
#




