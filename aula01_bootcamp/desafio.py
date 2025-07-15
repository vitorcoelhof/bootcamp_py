nome = input("qual o seu nome?")

salario = float(input("Qual o seu salário? "))

bonus = float(input("Qual o % do bônus? "))

bonus_final = 1000+salario * (bonus / 100)

print(f"Seu nome é {nome} , seu salário é R$ {salario} e o bônus final é R$ {bonus_final}")