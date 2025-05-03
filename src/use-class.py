from protocols.csv.csv_class import CsvProcessor

file_csv = 'src/data/exemplo.csv'
filtro = ['estado','preço']
limite = ['SP','10,21']

csv_processor = CsvProcessor(file_csv)

csv_processor.load_csv()
#print(csv_processor.filter_by(filtro, limite))
#print('#########################')
#print(csv_processor.sub_filter('preço', '10,80'))

print(csv_processor.recursive_filter(filtro, limite))