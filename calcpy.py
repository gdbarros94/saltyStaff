def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:  
        print("Divisão por 0.")
        return None

def banana ():
    while True:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            print(f"Resultado: {soma(num1, num2)}")
        elif operacao == '-':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif operacao == '*':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif operacao == '/':
            resultado = divisao(num1, num2)
            if resultado is not None:
                print(f"Resultado: {resultado}")
        else:
            print("Operação inválida!")
        
        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            break
    print("Saindo")

if __name__ == '__main__':
    banana()