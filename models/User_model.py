from database.bd import DatabaseManager

class UtilisateurModels ( DatabaseManager ):

    def ajouter_utilisateur(self, nom, prenom, role):
        self.cusor.execute('''INSERT INTO utilisateurs (nom, prenom, role) VALUES (?, ?, ?)''', 
                            (nom, prenom, role))
        self.conn.commit()
    
    def lister_utilisateurs(self):
        self.cusor.execute('''SELECT * FROM utilisateurs''')
        return self.cusor.fetchall()
    
    def supprimer_utilisateur(self, utilisateur_id):
        self.cusor.execute('''DELETE FROM utilisateurs WHERE id = ?''', (utilisateur_id,))
        self.conn.commit()
    
    def modifier_utilisateur(self, utilisateur_id, nouveau_role):
        self.cusor.execute('''UPDATE utilisateurs SET role = ? WHERE id = ?''', (nouveau_role, utilisateur_id))
        self.conn.commit()

    def rechercher_utilisateur(self, nom):
        self.cusor.execute('''SELECT * FROM utilisateurs WHERE nom = ?''', (nom,))
        return self.cusor.fetchone()