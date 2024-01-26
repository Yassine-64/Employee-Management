class IR:
    _tranches = [0, 28001, 40001, 50001, 60001, 150001]
    _tauxIR = [0, 0.12, 0.24, 0.34, 0.38, 0.40]

    @staticmethod
    def getIR(salaire):
        for i in range(1, 6):
            if salaire < IR._tranches[i]:
                return IR._tauxIR[i - 1]
        return IR._tauxIR[5]
