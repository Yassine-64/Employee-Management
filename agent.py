
from employee import Employe

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
