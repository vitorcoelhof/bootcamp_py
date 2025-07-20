import csv

caminho_do_arquivo = 'exemplo.csv'

dados = []

with open(file=caminho_do_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
        dados.append(linha)

print(dados)