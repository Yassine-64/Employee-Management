from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class IR:
    _tranches = [0, 28001, 40001, 50001, 60001, 150001]
    _tauxIR = [0, 0.12, 0.24, 0.34, 0.38, 0.40]

    @staticmethod
    def getIR(salaire):
        for i in range(1, 6):
            if salaire < IR._tranches[i]:
                return IR._tauxIR[i - 1]
        return IR._tauxIR[5]

class IEmploye(ABC):
    @abstractmethod
    def Age(self):
        pass

    @abstractmethod
    def Anciennete(self):
        pass

    @abstractmethod
    def DateRetraite(self, ageRetraite):
        pass

class Employe(IEmploye):
    cpt = 0

    def __init__(self, nom="", dateNaissance=datetime(2000, 1, 1), dateEmbauche=datetime.now(), salaireBase=0):
        Employe.cpt += 1
        self._mtle = Employe.cpt
        self._nom = nom
        self._dateNaissance = dateNaissance
        self.DateEmbauche = dateEmbauche
        self._salaireBase = salaireBase

    @property
    def Matricule(self):
        return self._mtle

    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, value):
        self._nom = value

    @property
    def DateNaissance(self):
        return self._dateNaissance

    @DateNaissance.setter
    def DateNaissance(self, value):
        if (value - self._dateNaissance).days / 365 < 16:
            raise Exception("L'âge au recrutement doit être supérieur à 16 ans")
        self._dateNaissance = value

    @property
    def DateEmbauche(self):
        return self._dateEmbauche

    @DateEmbauche.setter
    def DateEmbauche(self, value):
        if (value - self._dateNaissance).days / 365 < 16:
            raise Exception("L'âge au recrutement doit être supérieur à 16 ans")
        self._dateEmbauche = value

    @property
    def SalaireBase(self):
        return self._salaireBase

    @SalaireBase.setter
    def SalaireBase(self, value):
        self._salaireBase = value

    def Age(self):
        ts = datetime.now() - self._dateNaissance
        return int(ts.days / 365)

    def Anciennete(self):
        ts = datetime.now() - self._dateEmbauche
        return int(ts.days / 365)

    def DateRetraite(self, ageRetraite):
        ts = timedelta(days=ageRetraite * 365)
        dateRetraite = datetime(self._dateNaissance.year, self._dateNaissance.month, self._dateNaissance.day) + ts
        return dateRetraite

    @abstractmethod
    def SalaireAPayer(self):
        pass

    def __str__(self):
        return f"{self._mtle}-{self._nom}-{self._dateNaissance.strftime('%d/%m/%Y')}-{self._dateEmbauche.strftime('%d/%m/%Y')}-{self._salaireBase}"

    def __eq__(self, other):
        if isinstance(other, Employe):
            return self._mtle == other._mtle
        return False

class Formateur(Employe):
    _remunerationHSup = 70.00

    def __init__(self, nom="", dateNaissance=datetime(2000, 1, 1), dateEmbauche=datetime.now(), salaireBase=0, heureSup=0):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._heureSup = heureSup

    @property
    def HeureSup(self):
        return self._heureSup

    @HeureSup.setter
    def HeureSup(self, value):
        self._heureSup = value

    @staticmethod
    def RemunerationHSup():
        return Formateur._remunerationHSup

    def SalaireAPayer(self):
        NbreHS = self._heureSup
        if NbreHS >= 30:
            NbreHS = 30
        return (self._salaireBase + NbreHS * Formateur._remunerationHSup) * (1 - IR.getIR(self._salaireBase * 12))

    def __str__(self):
        return f"{super().__str__()}-{self._heureSup}"

class Agent(Employe):
    def __init__(self, nom="", dateNaissance=datetime(2000, 1, 1), dateEmbauche=datetime.now(), salaireBase=0, primeResponsabilite=0):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._primeResponsabilite = primeResponsabilite

    @property
    def PrimeResponsabilite(self):
        return self._primeResponsabilite

    @PrimeResponsabilite.setter
    def PrimeResponsabilite(self, value):
        self._primeResponsabilite = value

    def SalaireAPayer(self):
        return (self._salaireBase + self._primeResponsabilite) * (1 - IR.getIR(self._salaireBase * 12))
