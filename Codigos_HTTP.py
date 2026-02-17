#===============================================
#       HERRAMIENTA DE CHEQUEO DE URLS
#===============================================


import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# ==============================
# CONFIGURACIÓN
# ==============================
csv_path = "Base_de_datos.csv"
codigo_esperado = 200
MAX_WORKERS = 30
TIMEOUT = 12
CHUNK_SIZE = 500

# ==============================
# CARGA CSV
# ==============================
try:
    df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv(csv_path, sep=";", encoding="cp1252")

if "URL" not in df.columns:
    raise ValueError("El CSV debe tener una columna llamada 'URL'")

# ==============================
# SESSION POR HILO
# ==============================
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        retry = Retry(
            total=2,
            backoff_factor=0.4,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
            raise_on_status=False,
        )
        s = requests.Session()
        adapter = HTTPAdapter(
            max_retries=retry,
            pool_connections=MAX_WORKERS,
            pool_maxsize=MAX_WORKERS
        )
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        thread_local.session = s
    return thread_local.session

# ==============================
# WORKER
# ==============================
def check_url(row_dict):
    url = row_dict.get("URL")
    if not isinstance(url, str) or not url.strip():
        return None
    url = url.strip()

    try:
        session = get_session()
        r = session.get(url, timeout=TIMEOUT, allow_redirects=True)

        if r.status_code == codigo_esperado:
            print(f"[200 OK] {url}")  # 🔥 imprime la URL exitosa
            row_dict_out = dict(row_dict)
            row_dict_out["status_code"] = r.status_code
            return row_dict_out

        return None

    except requests.RequestException:
        return None

# ==============================
# EJECUCIÓN PARALELA
# ==============================
file_index = 1
buffer_ok = []
rows = df.to_dict(orient="records")

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = [executor.submit(check_url, row) for row in rows]

    for fut in as_completed(futures):
        result = fut.result()
        if result:
            buffer_ok.append(result)

            if len(buffer_ok) >= CHUNK_SIZE:
                output_path = f"output_ok_code_{codigo_esperado}_part_{file_index}.csv"
                pd.DataFrame(buffer_ok).to_csv(output_path, index=False)
                print(f"Archivo generado: {output_path}")
                buffer_ok.clear()
                file_index += 1

# Guardar lo restante
if buffer_ok:
    output_path = f"output_ok_code_{codigo_esperado}_part_{file_index}.csv"
    pd.DataFrame(buffer_ok).to_csv(output_path, index=False)
    print(f"Archivo generado: {output_path}")
