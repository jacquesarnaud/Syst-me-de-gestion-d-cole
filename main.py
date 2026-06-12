from config.Mes_constante import MENU_PRINCIPALE, OPTION_PRINCIPALE_ADMIN, GESTION_DES_ETUDIANTS, GESTION_DES_PROFESSEURS, GESTION_DES_MATIERES, GESTION_DES_NOTES
from utils.logger import LoggerUtils

def main():
    print(MENU_PRINCIPALE)
    while True:
        print(OPTION_PRINCIPALE_ADMIN)
        choix = input("Veuillez choisir une option : ")
        if choix == '1':
            print(GESTION_DES_ETUDIANTS)
            choix_etudiant = input("Veuillez choisir une option pour la gestion des étudiants : ")
            if choix_etudiant == '1':
                print("Ajouter un étudiant")
        elif choix == '2':
            print(GESTION_DES_PROFESSEURS)  
        elif choix == '3':
            print("Gestion des Utilisateurs")
        elif choix == '4':
            print(GESTION_DES_MATIERES)
        elif choix == '5':
            print(GESTION_DES_NOTES)
        elif choix == '6':
            print("Gestion des Absences")
        elif choix == '0':
            logger = LoggerUtils()
            logger.log_info("Application quittée par l'utilisateur.")
            break

if __name__ == "__main__":
    main()