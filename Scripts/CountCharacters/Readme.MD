### *Este script lee múltiples filas de una columna de un archivo CSV, calcula cuántos caracteres tiene cada fila y determina cuál es el texto con menor cantidad de caracteres (con un mínimo de 100).*



## Ventajas:

- Usa lectura eficiente con Polars.
- Permite manejar archivos con caracteres dañados (utf8-lossy).
- Filtra automáticamente valores nulos, vacíos o inválidos.
- Permite establecer un mínimo de caracteres (>= 100).
- Identifica rápidamente el texto más corto válido.



## Al finalizar:

- Muestra en consola el texto con menor cantidad de caracteres.
- Indica cuántos caracteres tiene.
- Indica el número de fila original donde se encuentra.



## En resumen:

Permite validar la calidad mínima del contenido en una columna específica y detectar textos que podrían estar incompletos o demasiado cortos.



## Dependencias

Necesitas instalar: **polars**

**Usa el siguiente comando:**

pip install polars



## Librerías utilizadas:

- polars → leer y analizar archivos CSV de forma rápida y eficiente.



## Cómo usarlo:

- Coloca tu archivo "metas.csv" en la misma carpeta.
- ASEGÚRATE de que tenga una columna llamada "goals".

**Ejecuta:**

python Cuenta_caracterez.py

**El resultado se mostrará directamente en la consola indicando:**

- Texto más corto válido.
- Cantidad de caracteres.
- Número de fila.

