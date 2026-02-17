# Este script lee un archivo CSV y mejora automáticamente el contenido de la columna "goals" utilizando la API de OpenAI, generando una versión optimizada y estandarizada de cada objetivo.



## Ventajas:

- Usa inteligencia artificial para mejorar la redacción de los objetivos.
- Procesa múltiples filas de forma automática.
- Utiliza un prompt previamente configurado en OpenAI.
- Respeta un rango de caracteres definido (entre 250 y 300).
- Permite mantener el resto de la información del CSV sin modificaciones.



## Al finalizar:

- Reemplaza el contenido original de la columna "goals" por una versión mejorada.
- Genera un nuevo archivo CSV con los cambios realizados.
- Mantiene la estructura original del archivo.
- Reproduce un sonido al finalizar el proceso.



## En resumen:

Automatiza la mejora y estandarización de objetivos usando inteligencia artificial, permitiendo optimizar grandes volúmenes de información de forma eficiente.



## Dependencias

Necesitas instalar: **pandas, openai & playsound**

**Usa el siguiente comando:**

pip install pandas  
pip install openai  
pip install playsound  



## Librerías utilizadas:

- pandas → leer y guardar archivos CSV.
- openai → conectar con la API de OpenAI para generar el texto mejorado.
- playsound → reproducir un sonido al finalizar el proceso.
- time → controlar pausas entre solicitudes a la API.



## Cómo usarlo:

- Coloca tu archivo "Base_de_datos.csv" en la misma carpeta.
- Configura tu API Key de OpenAI como variable de entorno o en un archivo llamado "OPENAI_API_KEY.env".

**Ejecuta:**

- python Enrich_Goals.py

**Se generará un archivo llamado:**

- Base_de_datos_goals_enriched.csv

### Este archivo contendrá la columna "goals" mejorada automáticamente.**



