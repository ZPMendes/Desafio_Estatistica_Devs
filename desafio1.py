import pandas as pd
import matplotlib.pyplot as plot

# Dicionário de Faturação

dict_faturacao = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

#Passar o Dicionário para Data Frame

df_faturacao = pd.DataFrame.from_dict(dict_faturacao)

#print(df_faturacao)

media_vendas = df_faturacao.valor.mean()

print(media_vendas)

#print(df_faturacao.dtypes) #usei para ver quais os data types dos values dentro do DataFrame

#df_faturacao['data_ref'] = pd.to_datetime(df_faturacao['data_ref'])

#print(df_faturacao.dtypes) #usei para ver se alterou o type do data_ref de 'objetct' para 'date_time'


plot.figure(figsize=(10,6))
df_faturacao.plot.bar(x='data_ref', y='valor', ax=plot.gca())
plot.title('Faturação por ano')
plot.xlabel('Ano')
plot.ylabel('Valor faturado')
plot.show()

plot.figure(figsize=(10,6))
df_faturacao.plot.line(x='data_ref', y='valor', ax=plot.gca())
plot.show()