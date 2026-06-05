from database.bd import DatabaseManager


class ProfesseurModels ( DatabaseManager ):

    def __init__(self):
        super().__init__()
        self.Professeur

    def Professeur (self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS professeurs  (      
            pof_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            matiere TEXT
            
        )
    """)
          
    def ajouter_professeur(self, nom, matiere):

        self.cusor.execute("INSERT INTO etudiants ( nom, matiere) VALUES (? , ?)",( nom,matiere))
        self.conn.commit()

    def modifier_professeur(self,professeur_id, matiere):
        self.cusor.execute('UPDATE etudiants SET  matiere= ? WHERE id = ?', (professeur_id, matiere))
        self.conn.commit()

    def suprimer_professeur  (self, professeur_id):
        self.cusor.execute("DELETE FROM etudiants WHERE id = ? ", (professeur_id,))
        self.conn.commit()

    def rechercher_professeur(self,professeur_id):

        self.cusor.execute('SELECT * FROM etudiants WHERE nom LIKE ?', ('%' + professeur_id + '%',))
        resultats = self.cusor.fetchall()
        return resultats

    def close(self):
        self.conn.close()
         