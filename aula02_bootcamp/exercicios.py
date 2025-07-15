# import math
# #exercicio 1 - Divisão Inteira

# valor_1 = int(input('Digite um número: '))
# valor_2 = int(input('Digite outro número: '))

# divisao = valor_1 // valor_2
# print("A divisão inteira de " + str(valor_1) + " por " + str(valor_2) + " é: " + str(divisao))
# print(f"A divisão inteira de {valor_1}  por  {valor_2} é {divisao}")

# #exercicio 2 - Area Circulo

# raio = float(input('Digite o raio '))
# area = math.pi*(raio**2)
# print(f"A área do círculo com raio {raio} é {area:2f}")

#datas

data_do_usuario = input('Insira uma data no formato dd/mm/aaaa:  ')

data_separada = data_do_usuario.split('/')

print(data_separada)

dia = int(data_separada[0])
mes = int(data_separada[1])
ano = int(data_separada[2])

print(f"A data informada é {dia} de {mes} de {ano}")