from database.bd import DatabaseManager
from models.Professeu_model import ProfesseurModels

class MatiereModels ( DatabaseManager ):

    def __init__(self):
        super().__init__()
        self.Matiere

    def Matiere(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS matiere (      
            matiere_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            FOREIGN KEY (pof_id) REFERENCES professeurs(pof_id)

        )
    """)
          
    def ajouter_matiere(self, nom,pof_id ):

        self.cusor.execute("INSERT INTO matiere (nom, teacher_id) VALUES (? , ?)",(nom,pof_id))
        self.conn.commit()

    def lister_matiere(self):
        self.cusor.execute("SELECT * FROM matiere ")
        return self.cusor.fetchall() 

    def affecter_matier(self,pof_id,id_matiere):
        self.cursor.execute('''
            INSERT INTO professeur (id_prof, matiere_id) 
            VALUES (?, ?)
        ''', (pof_id, id_matiere))
        self.conn.commit()

    def close(self):
        self.conn.close()
         