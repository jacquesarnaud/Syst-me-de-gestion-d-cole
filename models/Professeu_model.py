from database.bd import DatabaseManager


class ProfesseurModels ( DatabaseManager ):

    def ajouter_professeur(self, nom, prenom, matiere_id):
        self.cusor.execute('''INSERT INTO professeurs (nom, prenom, matiere_id) VALUES (?, ?, ?)''', 
                            (nom, prenom, matiere_id))
        self.conn.commit()
    
    def lister_professeurs(self):
        self.cusor.execute('''SELECT p.id, p.nom, p.prenom, m.nom_matiere 
                            FROM professeurs p 
                            JOIN matieres m ON p.matiere_id = m.id''')
        return self.cusor.fetchall()
    
    def supprimer_professeur(self, professeur_id):
        self.cusor.execute('''DELETE FROM professeurs WHERE id = ?''', (professeur_id,))
        self.conn.commit()
    
    def modifier_professeur(self, professeur_id, nouvelle_matiere_id):
        self.cusor.execute('''UPDATE professeurs SET matiere_id = ? WHERE id = ?''', (nouvelle_matiere_id, professeur_id))
        self.conn.commit()

    def rechercher_professeur(self, nom):
        self.cusor.execute('''SELECT p.id, p.nom, p.prenom, m.nom_matiere 
                            FROM professeurs p 
                            JOIN matieres m ON p.matiere_id = m.id
                            WHERE p.nom = ?''', (nom,))
        return self.cusor.fetchone()
    
    def affecter_matiere(self, professeur_id, matiere_id):
        self.cusor.execute('''UPDATE professeurs SET matiere_id = ? WHERE id = ?''', (matiere_id, professeur_id))
        self.conn.commit()