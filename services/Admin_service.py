#service administrateur
from database.bd import DatabaseManager
from models.User_model import UtilisateurModels
from models.Etudiant_model import EtudiantModels
from models.Absence_model import AbsenceModels  
from models.matiere_model import MatiereModels
from models.Professeu_model import ProfesseurModels

class AdminService:
    def __init__(self):
        self.etudiant_model = EtudiantModels()
        self.absence_model = AbsenceModels()
        self.matiere_model = MatiereModels()
        self.professeur_model = ProfesseurModels()

    def ajouter_etudiant(self, matricule, nom, prenom, age, classe):
        self.etudiant_model.ajouter_etudiant(matricule, nom, prenom, age, classe)   
    def lister_etudiants(self):
        return self.etudiant_model.lister_etudiants()
    def supprimer_etudiant(self, etudiant_id):
        self.etudiant_model.supprimer_etudiant(etudiant_id)
    def modifier_etudiant(self, etudiant_id, nouvelle_classe):
        self.etudiant_model.modifier_etudiant(etudiant_id, nouvelle_classe)
    def rechercher_etudiant(self, matricule):
        return self.etudiant_model.rechercher_etudiant(matricule)
    
    def ajouter_professeur(self, nom, prenom, matiere_id):
        self.professeur_model.ajouter_professeur(nom, prenom, matiere_id)
    def lister_professeurs(self):
        return self.professeur_model.lister_professeurs()
    def supprimer_professeur(self, professeur_id):
        self.professeur_model.supprimer_professeur(professeur_id)
    def modifier_professeur(self, professeur_id, nouvelle_matiere_id):
        self.professeur_model.modifier_professeur(professeur_id, nouvelle_matiere_id)
    def rechercher_professeur(self, nom):
        return self.professeur_model.rechercher_professeur(nom)
    def affecter_matiere(self, professeur_id, matiere_id):
        self.professeur_model.affecter_matiere(professeur_id, matiere_id)


    def ajouter_matiere(self, nom_matiere):
        self.matiere_model.ajouter_matiere(nom_matiere)
    def lister_matieres(self):
        return self.matiere_model.lister_matieres()     
    def supprimer_matiere(self, matiere_id):
        self.matiere_model.supprimer_matiere(matiere_id)
    def modifier_matiere(self, matiere_id, nouveau_nom):
        self.matiere_model.modifier_matiere(matiere_id, nouveau_nom)
    def rechercher_matiere(self, nom_matiere):
        return self.matiere_model.rechercher_matiere(nom_matiere)
    
    def ajouter_absence(self, etudiant_id, matiere_id, date, status):
        self.absence_model.ajouter_absence(etudiant_id, matiere_id, date, status)
    def lister_absences(self):
        return self.absence_model.lister_absences()
    def justifier_absence(self, absence_id):
        self.absence_model.justifier_absence(absence_id)
    def supprimer_absence(self, absence_id):
        self.absence_model.supprimer_absence(absence_id)
    def rechercher_absence_par_etudiant(self, etudiant_id):
        return self.absence_model.rechercher_absence_par_etudiant(etudiant_id)
    
    def moyenne_etudiant(self, etudiant_id):
        notes = self.etudiant_model.rechercher_note_par_etudiant(etudiant_id)
        if notes:
            total = sum(note[4] for note in notes)  # note[4] correspond à la colonne 'note'
            return total / len(notes)
        return None
    
    def moyenne_classe(self, classe):
        self.etudiant_model.cusor.execute('''SELECT e.id FROM etudiants e WHERE e.classe = ?''', (classe,))
        etudiants = self.etudiant_model.cusor.fetchall()
        if etudiants:
            total = 0
            count = 0
            for etudiant in etudiants:
                notes = self.etudiant_model.rechercher_note_par_etudiant(etudiant[0])  # etudiant[0] correspond à l'id de l'étudiant
                if notes:
                    total += sum(note[4] for note in notes)  # note[4] correspond à la colonne 'note'
                    count += len(notes)
            return total / count if count > 0 else None
        return None
    
    def meilleure_etudiant(self):
        self.etudiant_model.cusor.execute('''SELECT e.id, e.nom, e.prenom, AVG(n.note) as moyenne 
                                            FROM etudiants e 
                                            JOIN notes n ON e.id = n.etudiant_id 
                                            GROUP BY e.id 
                                            ORDER BY moyenne DESC 
                                            LIMIT 1''')
        return self.etudiant_model.cusor.fetchone() 