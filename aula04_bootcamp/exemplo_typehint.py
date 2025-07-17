# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

# Solicita ao usuário que digite seu nome
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while not nome_valido:
    try:
        nome:str = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif nome.isdigit():
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

while not salario_valido:
    try:
        salario: float = float(input("Digite o valor do seu salário: "))
        if float(salario) < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            print("Salário válido:", salario)
            salario_valido = True
    except ValueError as v:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        print(v)

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while not bonus_valido:
    try:
        bonus:float = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            print("Bonus válido:", bonus)
            bonus_valido = True
    except ValueError as t:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        print(t)
        

bonus_recebido = 1000 + salario * bonus  

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")