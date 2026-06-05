from database.bd import DatabaseManager

class UtilisateurModels ( DatabaseManager ):

    def __init__(self):
        super().__init__()
        self.Utilisateur

    def Utilisateur(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS utilisateur (      
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            role TEXT CHECK (role IN ('admin', 'professeur', 'etudiant'))
        )
    """)
          
    def ajouter_utilsateur(self, nom, role):

        self.cusor.execute("INSERT INTO utilisateur (nom, role) VALUES (? , ?)",(nom,role))
        self.conn.commit()

    def lister_utilsateur(self):
        self.cusor.execute("SELECT * FROM utilisateur ")
        return self.cusor.fetchall() 

    def suprimer_utilsateur(self, student_id):
        self.cusor.execute("DELETE FROM utilisateur WHERE id = ? ", (student_id,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
         