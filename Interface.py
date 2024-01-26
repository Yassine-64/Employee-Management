import tkinter as tk
from tkinter import ttk
from datetime import datetime
from agent import Agent
from formateur import Formateur
from payroll_system import *

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Employés")

        # Table to display the employees
        self.employees_table = ttk.Treeview(root, columns=("matricule", "nom", "date_naissance", "date_embauche", "salaire_base", "type", "heure_sup", "prime_responsabilite"), show="headings")
        self.employees_table.grid(row=7, column=0, columnspan=2)
        self.employees_table.heading("matricule", text="Matricule")
        self.employees_table.heading("nom", text="Nom")
        self.employees_table.heading("date_naissance", text="Date Naissance")
        self.employees_table.heading("date_embauche", text="Date Embauche")
        self.employees_table.heading("salaire_base", text="Salaire Base")
        self.employees_table.heading("type", text="Type")
        self.employees_table.heading("heure_sup", text="Heure Sup")
        self.employees_table.heading("prime_responsabilite", text="Prime Resp.")

        # Variable dial employee
        self.employee_name = tk.StringVar()
        self.employee_birthdate = tk.StringVar()
        self.employee_salary = tk.StringVar()
        self.employee_type = tk.StringVar(value="Agent")
        self.employee_overtime = tk.StringVar()
        self.employee_responsibility = tk.StringVar()

        tk.Label(root, text="Nom:").grid(row=0, column=0, sticky="e")
        tk.Entry(root, textvariable=self.employee_name).grid(row=0, column=1)

        tk.Label(root, text="Date Naissance:").grid(row=1, column=0, sticky="e")
        tk.Entry(root, textvariable=self.employee_birthdate).grid(row=1, column=1)

        tk.Label(root, text="Salaire de Base:").grid(row=2, column=0, sticky="e")
        tk.Entry(root, textvariable=self.employee_salary).grid(row=2, column=1)

        tk.Label(root, text="Type:").grid(row=3, column=0, sticky="e")
        tk.Radiobutton(root, text="Agent", variable=self.employee_type, value="Agent").grid(row=3, column=1, sticky="w")
        tk.Radiobutton(root, text="Formateur", variable=self.employee_type, value="Formateur").grid(row=3, column=1)

        tk.Label(root, text="Heure Sup").grid(row=4, column=0, sticky="e")
        tk.Entry(root, textvariable=self.employee_overtime).grid(row=4, column=1)

        tk.Label(root, text="Prime Responsabilité").grid(row=5, column=0, sticky="e")
        tk.Entry(root, textvariable=self.employee_responsibility).grid(row=5, column=1)

        tk.Button(root, text="Ajouter Employé", command=self.create_employee).grid(row=6, column=1, pady=10)

        # Charge les employés existants depuis le fichier lors du démarrage
        PayrollSystem.load_employees()

    def create_employee(self):
        # Create a new employee
        if self.employee_type.get() == "Agent":
            employee = Agent(
                nom=self.employee_name.get(),
                dateNaissance=datetime.strptime(self.employee_birthdate.get(), "%Y-%m-%d"),
                dateEmbauche=datetime.now(),
                salaireBase=float(self.employee_salary.get()),
                primeResponsabilite=float(self.employee_responsibility.get())
            )
        elif self.employee_type.get() == "Formateur":
            employee = Formateur(
                nom=self.employee_name.get(),
                dateNaissance=datetime.strptime(self.employee_birthdate.get(), "%Y-%m-%d"),
                dateEmbauche=datetime.now(),
                salaireBase=float(self.employee_salary.get()),
                heureSup=int(self.employee_overtime.get())
            )

        # Add the employee to the table
        if employee:
            PayrollSystem.add_employee(employee)
            self.employees_table.insert("", "end", values=(
                employee.Matricule,
                employee.Nom,
                employee.DateNaissance.strftime("%d/%m/%Y"),
                employee.DateEmbauche.strftime("%d/%m/%Y"),
                employee.SalaireBase,
                type(employee).__name__,
                getattr(employee, "HeureSup", ""),
                getattr(employee, "PrimeResponsabilite", "")
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
