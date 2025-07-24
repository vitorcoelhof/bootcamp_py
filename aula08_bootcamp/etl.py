import pandas as pd 
import os
import glob

# função de extract que le e consolida json
pasta = 'data'
def extrair_dados(pasta):
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# funcao que transforma

def calcular_kpi_de_total_de_vendas(df):
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# carregar dados

def carregar_dados(df, format_saida):
    """
    Carrega os dados em um formato específico.
    """
    for formato in format_saida:
        if formato == "csv":
            df.to_csv('vendas_consolidadas.csv', index=False)
        if formato == "parquet":
            df.to_parquet('vendas_consolidadas.parquet', index=False)
   

def pipeline(pasta,formato_de_saida):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)

    

    
    
    