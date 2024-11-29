from veiculo import Veiculo

class Moto(Veiculo):
    #mark: marca, model: modelo
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def fueltype(self):
        fueltype = str(input('Type of gasoline:'))
        return fueltype
    
    def passenger_capacity(self):
        return 'capacity of 2 passengers'