from database.bd import DatabaseManager


class EtudiantModels ( DatabaseManager ):
    
    def ajouter_etudiant(self, matricule, nom, prenom, age, classe):
        self.cusor.execute('''INSERT INTO etudiants (matricule, nom, prenom, age, classe) VALUES (?, ?, ?, ?, ?)''', 
                            (matricule, nom, prenom, age, classe))
        self.conn.commit()
    
    def lister_etudiants(self):
        self.cusor.execute('''SELECT * FROM etudiants''')
        return self.cusor.fetchall()
    
    def supprimer_etudiant(self, etudiant_id):
        self.cusor.execute('''DELETE FROM etudiants WHERE id = ?''', (etudiant_id,))
        self.conn.commit()
    
    def modifier_etudiant(self, etudiant_id, nouvelle_classe):
        self.cusor.execute('''UPDATE etudiants SET classe = ? WHERE id = ?''', (nouvelle_classe, etudiant_id))
        self.conn.commit()

    def rechercher_etudiant(self, matricule):
        self.cusor.execute('''SELECT * FROM etudiants WHERE matricule = ?''', (matricule,))
        return self.cusor.fetchone()