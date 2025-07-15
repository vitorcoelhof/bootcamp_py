import math
#exercicio 1 - Divisão Inteira

valor_1 = int(input('Digite um número: '))
valor_2 = int(input('Digite outro número: '))

divisao = valor_1 // valor_2
print("A divisão inteira de " + str(valor_1) + " por " + str(valor_2) + " é: " + str(divisao))
print(f"A divisão inteira de {valor_1}  por  {valor_2} é {divisao}")

#exercicio 2 - Area Circulo

raio = float(input('Digite o raio '))
area = math.pi*(raio**2)
print(f"A área do círculo com raio {raio} é {area:2f}")