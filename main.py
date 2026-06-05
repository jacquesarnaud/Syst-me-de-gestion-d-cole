

from models.Etudiant_model import EtudiantModels
from models.matiere_model import MatiereModels


user = EtudiantModels()
list= (user.liter_etudiants())
for (id) in list:
    print(id )
user.close




