from calculadora import Calculadora

def menu():
    print("\nEscolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")


calc = Calculadora()
while True:
    menu()
    escolha = input("Digite o número da operação: ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.operacao(escolha, num1, num2)
        print(f"Resultado: {resultado}")
    else:
        print("Saindo...")
        break