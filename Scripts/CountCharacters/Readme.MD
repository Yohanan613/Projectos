# *Este script lee un archivo CSV y analiza una columna llamada "goals" para encontrar el texto más corto que tenga al menos 100 caracteres.*
#
# Ventajas:
 - Filtra automáticamente valores vacíos, nulos o incorrectos.
 - Cuenta los caracteres de cada texto de forma rápida y eficiente.
 - Ordena los resultados automáticamente.
#
# Al finalizar:
 - Muestra en consola el texto más corto válido.
 - Indica cuántos caracteres tiene.
 - Indica en qué número de fila se encuentra.
#
# En resumen:
 Permite detectar textos demasiado cortos y validar la calidad mínima del contenido.
#

# Dependencias

Necesitas instalar: **polars**

**Usa el siguiente comando:**
  -pip install polars

# Librerías utilizadas:
 - polars → leer y analizar archivos CSV de forma rápida

# Cómo usarlo:
 - Coloca tu archivo "metas.csv" en la misma carpeta.
 - ASEGURATE de que tenga una columna llamada "goals".

 Ejecuta:
 python Cuenta_caracterez.py

 El resultado se mostrará directamente en la consola.
#

