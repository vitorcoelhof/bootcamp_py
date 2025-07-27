from src.csv_classes import CsvProcessor

arquivo_csv = 'data/exemplo.csv'
filtro = 'estado'
limite = 'SP'

limite2 = 'DF'

arquivo_csv = CsvProcessor(arquivo_csv)
arquivo_csv.load_csv()
print(arquivo_csv.filter_by_estado(filtro, limite))
print('########################')
print(arquivo_csv.filter_by_estado(filtro, limite2))