from datetime import datetime
from formateur import Formateur
from agent import Agent
from payroll_system import PayrollSystem

if __name__ == "__main__":
    while True:
        PayrollSystem.show_menu()
        choice = input("Choix (1, 2, 3, 4): ")

    if choice == "1":
            PayrollSystem.display_employees()

        elif choice == "2":
            employee_type = input("Type d'employé (Formateur/Agent): ")
            nom = input("Nom de l'employé: ")
            date_naissance = datetime.strptime(input("Date de naissance (YYYY-MM-DD): "), "%Y-%m-%d")
            date_embauche = datetime.now()  # Set default to current date
            salaire_base = float(input("Salaire de base: "))

            if employee_type.lower() == "formateur":
                heure_sup = int(input("Heures supplémentaires: "))
                new_employee = Formateur(nom, date_naissance, date_embauche, salaire_base, heure_sup)
            elif employee_type.lower() == "agent":
                prime_responsabilite = float(input("Prime de responsabilité: "))
                new_employee = Agent(nom, date_naissance, date_embauche, salaire_base, prime_responsabilite)
            else:
                print("Type d'employé non reconnu.")
                continue

            PayrollSystem.add_employee(new_employee)

        elif choice == "3":
            matricule = int(input("Matricule de l'employé à supprimer: "))
            PayrollSystem.remove_employee(matricule)

        elif choice == "4":
            print("Programme terminé.")
            break

        else:
            print("Option non valide. Veuillez choisir parmi les options disponibles.")
