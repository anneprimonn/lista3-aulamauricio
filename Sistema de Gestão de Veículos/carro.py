from veiculo import Veiculo

class Carro(Veiculo):
    #mark: marca, model: modelo
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def fueltype():
        fueltype = str(input('Type of gasoline:'))
        return fueltype
    
    def passenger_capacity():
        return ('capacity of 5 passengers')