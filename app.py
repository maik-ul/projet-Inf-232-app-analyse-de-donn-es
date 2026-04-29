from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Configuration de la base de données
DB_PATH = 'recensement.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS citoyens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            age INTEGER,
            quartier TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return  render_template('interface user.html')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM citoyens')
    habitants = cursor.fetchall()
    conn.close()
    return render_template('index.html', habitants=habitants)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    age = request.form.get('age')
    quartier = request.form.get('quartier')

    if nom and prenom:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO citoyens (nom, prenom, age, quartier) VALUES (?, ?, ?, ?)',
                       (nom, prenom, age, quartier))
        conn.commit()
        conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)