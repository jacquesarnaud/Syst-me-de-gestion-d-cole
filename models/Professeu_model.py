from 
class ProfesseurModels ( DatabaseManager ):

    def __init__(self):
        super().__init__(self)


    def Professeur (self):
        self.cusor.connecte("""
            CREATE TABLE IF EXISTE professeur (      
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            matiere TEXT
        )
    """)
          
    def ajouter_professeur(self, nom, matiere):

        self.cusor.execute("INSERT INTO professeur (nom, age) VALUES (? , ?)",(nom,matiere))
        self.conn.commit()

    def afficher_professeur(self):
        self.cusor.execute("SELECT * FROM professeur ")
        return self.cusor.fetchall() 

    def suprimer_professeur(self, nom):
        self.cusor.execute("DELETE FROM professeur WHERE id = ? ", (nom,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
         