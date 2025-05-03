import pandas as pd

file_csv = './exemplo.csv'

df = pd.read_csv(file_csv)

df_filtrado = df[df['estado'] == 'SP']

print(df_filtrado)