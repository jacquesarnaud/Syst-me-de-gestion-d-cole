from database.bd import DatabaseManager

class UtilisateurModels ( DatabaseManager ):

    def __init__(self):
        super().__init__()
        self.Utilisateur()

    def Utilisateur(self):
        self.cusor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin', 'etudiant', 'professeur')),
        email TEXT UNIQUE NOT NULL,
        mot_de_passe TEXT NOT NULL
    )
    """)
        
    def supp_table(self,nom_table):
        self.cusor.execute(f"DROP TABLE IF EXISTS {nom_table}")
        self.conn.commit()

    def ajouter_utilsateur(self, nom, role,email,mot_de_passe):

        self.cusor.execute("INSERT INTO utilisateur (nom, role,email,mot_de_passe) VALUES (? , ?)",(nom, role,email,mot_de_passe))
        self.conn.commit()

    def lister_utilsateur(self):
        self.cusor.execute("SELECT * FROM utilisateur ")
        return self.cusor.fetchall() 

    def suprimer_utilsateur(self, email):
        self.cusor.execute("DELETE FROM utilisateur WHERE id = ? ", (email,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
         