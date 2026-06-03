from database import*


class EtudiantModels ( DatabaseManager ):

    def __init__(self):
        super().__init__(self)


    def Etudiant (self):
        self.cusor.connecte("""
            CREATE TABLE IF EXISTE etudiants  (      
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricule TEXT,
            nom TEXT,
            prenom TEXT,
            age INTEGER,
            classe TEXT
        )
    """)
          
    def ajouter_etudiants(self, matricule,nom, prenom,age,classe):

        self.cusor.execute("INSERT INTO etudiants ( matricule,nom, prenom,age,classe) VALUES (? , ?)",( matricule,nom, prenom,age,classe))
        self.conn.commit()

    def afficher_etudiants(self):
        self.cusor.execute("SELECT * FROM etudiants ")
        return self.cusor.fetchall() 

    def suprimer_etudiants  (self, matricule):
        self.cusor.execute("DELETE FROM etudiants WHERE id = ? ", (matricule,))
        self.conn.commit()

    def close(self):
        self.conn.close()
         