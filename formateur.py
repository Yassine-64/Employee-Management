from employee import Employe

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
