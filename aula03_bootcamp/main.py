salario_valido = False

while not salario_valido:
    try:
        salario = input("Digite o valor do seu salário: ")
        if salario.isalpha() == True:
            print("Por favor, digite um número positivo para o salário.")
        elif float(salario) < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            print("Salário válido:", salario)
            salario_valido = True
    except ValueError as v:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        print(v)