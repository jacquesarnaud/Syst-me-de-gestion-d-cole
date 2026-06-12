import sqlite3

class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect("./database/BASSE.db")
        self.cusor = self.conn.cursor()
    
    def create_tables(self):
        self.cusor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom TEXT NOT NULL,
                                prenom TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                mot_de_passe TEXT NOT NULL,
                                role TEXT NOT NULL check(role IN ('admin', 'professeur', 'etudiant'))
                            )''')

        self.cusor.execute('''CREATE TABLE IF NOT EXISTS professeurs (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom TEXT NOT NULL,
                                matiere_id INTEGER,
                                FOREIGN KEY (matiere_id) REFERENCES matieres(id)
                            )''')

        self.cusor.execute('''CREATE TABLE IF NOT EXISTS etudiants (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                matricule TEXT NOT NULL UNIQUE,
                                nom TEXT NOT NULL,
                                prenom TEXT NOT NULL,
                                age INTEGER NOT NULL,
                                classe TEXT NOT NULL
                            )''')

        self.cusor.execute('''CREATE TABLE IF NOT EXISTS matieres (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom_matiere TEXT NOT NULL UNIQUE
                            )''')
        
        self.cusor.execute('''CREATE TABLE IF NOT EXISTS notes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                etudiant_id INTEGER NOT NULL,
                                matiere_id INTEGER NOT NULL,
                                note REAL NOT NULL, 
                                FOREIGN KEY (etudiant_id) REFERENCES etudiants(id), 
                                FOREIGN KEY (matiere_id) REFERENCES matieres(id)
                            )''')
        
        self.cusor.execute('''CREATE TABLE IF NOT EXISTS absences (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                etudiant_id INTEGER NOT NULL,
                                matiere_id INTEGER NOT NULL,
                                date TEXT NOT NULL, 
                                FOREIGN KEY (etudiant_id) REFERENCES etudiants(id), 
                                FOREIGN KEY (matiere_id) REFERENCES matieres(id),
                                status TEXT NOT NULL CHECK(status IN ('justifiée', 'non justifiée'))
                            )''')
                        

        self.conn.commit()