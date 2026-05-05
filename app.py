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
            ville TEXT
            Departement TEXT
             Region TEXT             
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
    return render_template('interface user.html', habitants=habitants)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    age = request.form.get('age')
    ville = request.form.get('ville')
    Departement = request.form.get('Département')
    Region= request.form.get(('region'))

    if nom and prenom:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO citoyens (nom, prenom, age, ville,Departement,Région) VALUES (?, ?, ?, ?,?,?)',
                       (nom, prenom, age, ville, Departement, Region))
        conn.commit()
        conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)