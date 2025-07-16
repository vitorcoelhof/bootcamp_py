#exercicio 1 - checar valores
# Verifica se os valores são positivos

# quantidade = 40
# preco = 20

# if quantidade > 0 and preco > 0:
#     print('valores validos')
# else:
#     print('valores invalidos')


#exercicio 2 - utilizando for


# lista_de_alunos = ["Vitor", "João", "Maria", "Ana", "Pedro"]

# for aluno in lista_de_alunos:
#     print(aluno)

texto = "hoje e a nossa segunda aula do bootcamp , bootcamp de python"

palavras = texto.split(" ")

print(palavras)

contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1