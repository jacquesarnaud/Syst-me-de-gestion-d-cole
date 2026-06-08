from database.bd import DatabaseManager
from models.Professeu_model import ProfesseurModels

class NotesModels ( DatabaseManager ):

    def __init__(self):
        super().__init__()
        self.Notes

    def Notes(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS notes (      
            notes_id INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY (etud_id) REFERENCES etudiants(etud_id),
            FOREIGN KEY (matiere_id) REFERENCES matiere(matiere_id),
            note INTEGER 

        )
    """)
          
    def ajouter_note(self,etud_id,matiere_id ,note):

        self.cusor.execute("INSERT INTO notes (etud_id, matiere_id,note) VALUES (? , ?)",(etud_id,matiere_id ,note))
        self.conn.commit()

    
    def modifier_note(self,etud_id, nouvelle_note):
        self.cusor.execute('UPDATE notes SET note = ? WHERE id = ?', (etud_id, nouvelle_note))
    
    def suprimer_note(self, etud_id):
        self.cusor.execute("DELETE FROM notes WHERE id = ? ", (etud_id,))
        self.conn.commit()

    def Calculer_moyenne(self):
        pass

    def close(self):
        self.conn.close()
         