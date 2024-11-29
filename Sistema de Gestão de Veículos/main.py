from moto import Moto
from carro import Carro
from caminhao import Caminhao

def main():
    moto = Moto('Yamaha,', 'XTZ 250')
    print(f'\nMoto: {moto.brand} {moto.model}')
    print(f'Combustível: {moto.fueltype()}')
    print(f'Capacidade: {moto.passenger_capacity()}')

    caminhão = Caminhao('Volkswagen,', 'VW Meteor')
    print(f'\nCaminhão: {caminhão.brand} {caminhão.model}')
    print(f'Combustível: {caminhão.fueltype()}')
    print(f'Capacidade: {caminhão.passenger_capacity()}')

    carro = Carro('Ford,', 'Ford Ka')
    print(f'\nCarro: {carro.brand} {carro.model}')
    print(f'Combustível: {carro.fueltype()}')
    print(f'Capacidade: {carro.passenger_capacity()}')

if __name__ == '__main__':
    main()
