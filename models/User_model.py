from database import bd

class UtilisateurModels ( DatabaseManager ):

    def __init__(self):
        super().__init__(self)


    def Utilisateur(self):
        self.cusor.connecte("""
            CREATE TABLE IF EXISTE utilisateur (      
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            role INTEGER
        )
    """)
          
    def ajouter_utilsateur(self, nom, role):

        self.cusor.execute("INSERT INTO utilisateur (nom, age) VALUES (? , ?)",(nom,role))
        self.conn.commit()

    def afficher_utilsateur(self):
        self.cusor.execute("SELECT * FROM utilisateur ")
        return self.cusor.fetchall() 

    def suprimer_utilsateur(self, student_id):
        self.cusor.execute("DELETE FROM utilisateur WHERE id = ? ", (student_id,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
         