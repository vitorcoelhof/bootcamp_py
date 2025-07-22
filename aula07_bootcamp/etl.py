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



def filtrar_produtos_nao_entregues(lista):
    """Filtra os produtos que não foram entregues."""
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto['entregue'] == 'True':
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados):
    """Soma os valores dos produtos filtrados."""
    soma = 0
    for produto in lista_com_produtos_filtrados:
        soma += float(produto.get('price'))
    return soma


lista_produtos = ler_csv(path_arquivos)
produtos_entregues = filtrar_produtos_nao_entregues(lista_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)



print(lista_produtos)
print(produtos_entregues)
print(valor_dos_produtos_entregues)