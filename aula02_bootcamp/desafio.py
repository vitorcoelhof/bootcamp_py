nome = input("qual o seu nome?")

if nome.isdigit():
    print("O nome não pode ser um número.")
elif len(nome) == 0:
    print("O nome não pode ficar em branco.")
elif nome.isspace():
    print("O nome não pode conter apenas espaços.")
else:
    print(nome)
    exit()


# salario = float(input("Qual o seu salário? "))

# bonus = float(input("Qual o % do bônus? "))

# bonus_final = 1000+salario * (bonus / 100)

# print(f"Seu nome é {nome} , seu salário é R$ {salario} e o bônus final é R$ {bonus_final}")


