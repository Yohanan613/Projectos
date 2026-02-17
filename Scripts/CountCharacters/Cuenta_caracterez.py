#Este archivo permite leer multiples filas de una columna de un archivo csv.
#Cuantos caracterez tiene cada fila de la columna y cual es el que menos caracteres tiene.

import polars as pl

archivo = "metas.csv"
columna = "goals"

# Some rows have non‑UTF8 bytes; read lossy to avoid the crash.
df = pl.read_csv(
    archivo,
    columns=[columna],
    encoding="utf8-lossy",
    truncate_ragged_lines=True,
).with_row_count("fila")

df = df.filter(pl.col(columna).is_not_null() & (pl.col(columna) != "")  &  (pl.col(columna) != "null")  & (pl.col(columna).str.len_chars() >= 100))

resultado = (

    df.with_columns(pl.col(columna).str.len_chars().alias("length"))
         .sort("length")
         .head(1)
)

print("Texto:", resultado[columna][0])
print("Cantidad de caracteres:", resultado["length"][0])
print("Fila:", resultado["fila"][0])
