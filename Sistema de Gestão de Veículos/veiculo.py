class Veiculo():
     #mark: marca, model: modelo
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def fueltype(self):
        return 'Desconhecido'
    
    def passenger_capacity(self):
        return 0