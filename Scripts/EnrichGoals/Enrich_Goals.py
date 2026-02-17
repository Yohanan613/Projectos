# =========================================================
# enrich_goals_from_context.py
# =========================================================

import os
import json
import pandas as pd
import time
import csv
from openai import OpenAI
from playsound import playsound


#=========================================================================
#                         CONFIGURACIÓN
# ========================================================================

INPUT_FILE = "Base_de_datos_7.csv"
OUTPUT_FILE = "Base_de_datos_goals_enriched_7.csv"

# Prompt guardado en OpenAI (el tuyo)
OPENAI_PROMPT_ID = "pmpt_6993622c1c788196b5037e69c5ece5ac00d48254343da37b"
PROMPT_VERSION = "5"

GOALS_COL = "goals"
DESC_COL = "description"


# ==========================================================================

def load_api_key():
    # 1) Standard env var
    key = os.environ.get("OPENAI_API_KEY")
    if key and key.strip():
        return key.strip()

    # 2) Fallback to local env file
    env_path = "OPENAI_API_KEY.env"
    if os.path.isfile(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Accept "OPENAI_API_KEY=...."
                if line.startswith("OPENAI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")

                # Or if file contains only the key
                return line.strip().strip('"').strip("'")

    return None


api_key = load_api_key()
if not api_key:
    raise RuntimeError(
        "No se encontró OPENAI_API_KEY. Define la variable de entorno OPENAI_API_KEY "
        "o crea el archivo OPENAI_API_KEY.env con la línea OPENAI_API_KEY=tu_key."
    )

client = OpenAI(api_key=api_key)


def is_empty(value):
    if value is None:
        return True
    if isinstance(value, float) and pd.isna(value):
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    return False


def _ensure_250_300(text: str) -> str:
    """
    Si el modelo devuelve algo fuera de 250–300 chars, lo ajustamos:
    - Si es >300, recorta a 300.
    - Si es <250, lo dejamos tal cual (mejor no inventar); idealmente el prompt lo cumple.
    """
    if not text:
        return ""
    t = " ".join(text.split())  # normaliza espacios
    if len(t) > 300:
        t = t[:300].rstrip()
    return t


# ---------------- OpenAI call ----------------
def rewrite_goals_from_row(row_dict: dict) -> str:
    """
    Envía la fila completa como JSON string.
    El prompt retorna SOLO texto (resumen 250–300 chars).
    """
    payload = json.dumps(row_dict, ensure_ascii=False)

    response = client.responses.create(
        prompt={"id": OPENAI_PROMPT_ID, "version": PROMPT_VERSION},
        input=payload,
    )

    text = getattr(response, "output_text", "") or ""
    text = text.strip()
    print(f"Respuesta OpenAI (len={len(text)}): {text}")

    return _ensure_250_300(text)


# ---------------- MAIN ----------------
def main():
    df = None
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            df = pd.read_csv(
                INPUT_FILE,
                sep=";",
                dtype=str,
                keep_default_na=False,
                encoding=enc,
                engine="python",
            )
            print(f"Leído {INPUT_FILE} con encoding: {enc}")
            break
        except UnicodeDecodeError:
            continue

    if df is None:
        raise UnicodeDecodeError(
            "utf-8",
            b"",
            0,
            1,
            f"No se pudo leer {INPUT_FILE} con codificaciones conocidas.",
        )

    # Validación de columnas
    if GOALS_COL not in df.columns:
        raise ValueError(f"No existe la columna '{GOALS_COL}' en el CSV.")
    if DESC_COL not in df.columns:
        print(f"⚠️ No existe la columna '{DESC_COL}'. Se usará solo goals.")

    for idx, row in df.iterrows():
        goals_value = row.get(GOALS_COL, "")
        desc_value = row.get(DESC_COL, "") if DESC_COL in df.columns else ""

        # Caso 1: goals vacío -> usar description como contexto
        # Caso 2: ambos vacíos -> dejar en blanco y no llamar a OpenAI
        if is_empty(goals_value) and is_empty(desc_value):
            df.at[idx, GOALS_COL] = ""
            print(f"Fila {idx}: goals y description vacíos -> se deja en blanco")
            continue

        # Construir dict con TODA la fila para contexto
        row_dict = row.to_dict()

        # Si goals está vacío, pero description no: ponemos goals=description
        # para que el prompt “especialmente goals” tenga algo que resumir.
        if is_empty(goals_value) and not is_empty(desc_value):
            row_dict[GOALS_COL] = desc_value

        print(f"Procesando fila {idx}...")

        new_goals = rewrite_goals_from_row(row_dict)

        # Reemplaza SOLO la columna goals, sin tocar las demás
        df.at[idx, GOALS_COL] = new_goals if not is_empty(new_goals) else ""

        time.sleep(2)

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        sep=";",
        encoding="utf-8-sig",
        quoting=csv.QUOTE_MINIMAL,
    )

    print(f"Archivo generado: {OUTPUT_FILE}")
    playsound("termino.mp3")


if __name__ == "__main__":
    main()
