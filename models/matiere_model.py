from database.bd import DatabaseManager

class MatiereModels ( DatabaseManager ):
    def ajouter_matiere(self, nom_matiere):
        self.cusor.execute('''INSERT INTO matieres (nom_matiere) VALUES (?)''', (nom_matiere,))
        self.conn.commit()
    
    def lister_matiere(self):
        self.cusor.execute('''SELECT * FROM matieres''')
        return self.cusor.fetchall()
    
    def supprimer_matiere(self, matiere_id):
        self.cusor.execute('''DELETE FROM matieres WHERE id = ?''', (matiere_id,))
        self.conn.commit()
    
    def modifier_matiere(self, matiere_id, nouveau_nom):
        self.cusor.execute('''UPDATE matieres SET nom_matiere = ? WHERE id = ?''', (nouveau_nom, matiere_id))
        self.conn.commit()

    def rechercher_matiere(self, nom_matiere):
        self.cusor.execute('''SELECT * FROM matieres WHERE nom_matiere = ?''', (nom_matiere,))
        return self.cusor.fetchone()