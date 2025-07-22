from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_dos_produtos 

path_arquivos = 'vendas.csv'

lista_produtos = ler_csv(path_arquivos)
produtos_entregues = filtrar_produtos_nao_entregues(lista_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)

print(lista_produtos)
print(produtos_entregues)
print(valor_dos_produtos_entregues)
