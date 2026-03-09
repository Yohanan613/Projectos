from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3 as sq

app = Flask(__name__)
CORS(app)

DB = "tareas.db"

def conectar_db():
    conn = sq.connect(DB)
    conn.row_factory = sq.Row
    return conn

def inicio_db():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            estado INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Obtener tareas
@app.route("/tareas")
def obtener_tareas():
    conn = conectar_db()
    tareas = conn.execute("SELECT * FROM tareas ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(t) for t in tareas])


# Crear tarea
@app.route("/tareas", methods=["POST"])
def crear_tarea():
    data = request.json

    conn = conectar_db()
    conn.execute(
        "INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, 0)",
        (data["titulo"], data["descripcion"])
    )
    conn.commit()
    conn.close()

    return {"status": "ok"}


# mover tarea
@app.route("/tareas/<int:id_tarea>", methods=["PUT"])
def mover_tarea(id_tarea):
    data = request.json

    conn = conectar_db()
    conn.execute(
        "UPDATE tareas SET estado=? WHERE id=?",
        (data["estado"], id_tarea)
    )
    conn.commit()
    conn.close()

    return {"status": "ok"}


if __name__ == "__main__":
    inicio_db()
    app.run(debug=True)