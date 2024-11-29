from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

class Calculadora:
    def __init__(self):
        self.soma = Soma()
        self.subtracao = Subtracao()
        self.multiplicacao = Multiplicacao()
        self.divisao = Divisao()

    def operacao(self, escolha, num1, num2):
        if escolha == '1':  # Soma
            return self.soma.calcular(num1, num2)
        elif escolha == '2':  # Subtração
            return self.subtracao.calcular(num1, num2)
        elif escolha == '3':  # Multiplicação
            return self.multiplicacao.calcular(num1, num2)
        elif escolha == '4':  # Divisão
            return self.divisao.calcular(num1, num2)
        else:
            return "Operação inválida!"
