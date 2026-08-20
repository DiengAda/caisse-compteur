from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

BILLETS = [5, 10, 20, 50, 100, 200, 500]
PIECES = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]

@app.route("/")
def index():
    return render_template("index.html", billets=BILLETS, pieces=PIECES)

@app.route("/api/comptage", methods=["POST"])
def enregistrer_comptage():
    data = request.get_json()
    montant = data.get("total")

    conn = sqlite3.connect("caisse.db")
    conn.execute(
        "INSERT INTO comptages (date_comptage, montant_compte) VALUES (?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), montant)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True})


# fonction pour la table de la base de données
def init_db():
    conn = sqlite3.connect("caisse.db")
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS comptages (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date_comptage TEXT NOT NULL,
                     montant_compte REAL NOT NULL)
                     """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    