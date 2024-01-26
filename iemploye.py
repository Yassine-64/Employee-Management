from abc import ABC, abstractmethod
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
