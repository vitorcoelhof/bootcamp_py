#utilizando try e except para tratar erros de divisão por zero
try:
    valor_1 = int(input('Digite um número: '))
    valor_2 = int(input('Digite outro número: '))
    divisao = valor_1 // valor_2
except ZeroDivisionError:
    print("integer division or modulo by zero")
except KeyboardInterrupt:
    print("Operação cancelada pelo usuário.")
else:
    print(f"A divisão inteira de {valor_1} por {valor_2} é: {divisao}. Deu tudo certo!")
finally: 
    print("Fim do programa.")


# verificando se o valor é um número inteiro
valor_1 = input('Digite um número: ')
if isinstance(valor_1, int):
    print("O primeiro valor é um número inteiro.")
else:
    print("O primeiro valor não é um número inteiro.")


#verificando idade

idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
