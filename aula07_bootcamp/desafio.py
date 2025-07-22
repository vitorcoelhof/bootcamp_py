import pandas as pd
import csv

path_arquivos = 'vendas.csv'

def ler_csv(arquivo):
    """Função para ler um arquivo CSV e retornar uma lista de dicionários."""
    lista = []
    with open(arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)  # ✅ CORRIGIDO: usar 'file' em vez de 'arquivo'
        for linha in leitor:
            lista.append(linha)
    return lista

vendas_itens = ler_csv(path_arquivos)
print(vendas_itens)