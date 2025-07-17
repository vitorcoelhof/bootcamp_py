livro_01 = {
    "titulo": "Aprendendo Python",
    "autor": "João da Silva",
    "ano_publicacao": 2021,
    "preco": 49.90,
    "disponivel": True,
}

livro_02 = {
    "titulo": "Python para Iniciantes",
    "autor": "Maria Oliveira",
    "ano_publicacao": 2020,
    "preco": 39.90,
    "disponivel": False,
}

livro = []

livro.append(livro_01)
livro.append(livro_02)

print(livro)

lista_de_livros_dic = {
    "livro_01": {"titulo": "Aprendendo Python",
    "autor": "João da Silva",
    "ano_publicacao": 2021,
    "preco": 49.90,
    "disponivel": True},

    "livro_02": {
    "titulo": "Python para Iniciantes",
    "autor": "Maria Oliveira",
    "ano_publicacao": 2020,
    "preco": 39.90,
    "disponivel": False}
}

print(lista_de_livros_dic)
print(lista_de_livros_dic["livro_01"]["titulo"])