from etl import pipeline

pasta = 'data'
formato_de_saida = ['csv', 'parquet']

pipeline(pasta, formato_de_saida)
