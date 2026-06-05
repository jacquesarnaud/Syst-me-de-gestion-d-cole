from database.bd import DatabaseManager


class EtudiantModels ( DatabaseManager ):

    def __init__(self):
        super().__init__()
        self.Etudiant()

    def Etudiant (self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS etudiants  (      
            etud_id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricule TEXT NOT NULL,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            age INTEGER,
            classe TEXT 
        )
    """)
          
    def ajouter_etudiants(self, matricule,nom, prenom,age,classe):

        self.cusor.execute(
            "INSERT INTO etudiants (matricule, nom, prenom, age, classe) VALUES (?, ?, ?, ?, ?)",
            (matricule, nom, prenom, age, classe))   
        self.conn.commit()

    def modifier_etudiant(self,etudiant_id, nouvelle_classe):
        self.cusor.execute('UPDATE etudiants SET classe = ? WHERE id = ?', (nouvelle_classe, etudiant_id))
    
    def suprimer_etudiants  (self, matricule):
        self.cusor.execute("DELETE FROM etudiants WHERE etud_id = ? ", (matricule,))
        self.conn.commit()

    def liter_etudiants(self):
        self.cusor.execute("SELECT * FROM etudiants ")
        return self.cusor.fetchall() 


    def rechercher_etudiant(self,matricule):

        self.cusor.execute('SELECT * FROM etudiants WHERE nom LIKE ?', ('%' + matricule + '%',))
        resultats = self.cusor.fetchall()
        return resultats

    def close(self):
        self.conn.close()
         