# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:07:04 2021

@author: arthur
"""
import pandas as pd
import numpy as np
import csv


path = '/home/oem/Documents/fractal/arquivos/Chuvas_CFS'


#Abre o arquivo de chuvas e transpões a matriz,usando csv puro
importa_dados = csv.reader(open(path + '/chuva_CFS_amazonia.txt'))
importa_dados = [i for i in importa_dados]
importa_dados = [i[0].split("   ")[1:] for i in importa_dados]
importa_dados = np.array(importa_dados)
arquivo_original_csv = importa_dados.astype(float)
arquivo_transposto_csv = arquivo_original_csv.T

#Declara as variaveis para gerar o dataframe final
bacias = ["amazonia", "uruguai", "tocantins", "tiete", "paranapanema", "iguacu", "grande"]

lista_dados_chuva = [i1[i2] for i1 in arquivo_transposto_csv for i2 in range(0,12)]

lista_anos = [i for i in range(1979, 2023, 1)]*12
lista_anos.sort()

lista_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
lista_meses = lista_meses*44

df_dados_fornecidos_global = pd.DataFrame(columns=['Bacia', 'Ano', 'Mes', 'Precipitacao'])

#Loop para filtrar os dados por bacia e inserir no dataframe
for item in bacias:
    importa_dados = csv.reader(open(path + '/chuva_CFS_%s.txt'%item))
    importa_dados = [i for i in importa_dados]
    importa_dados = [i[0].split("   ")[1:] for i in importa_dados]
    importa_dados = np.array(importa_dados)
    arquivo_original_csv = importa_dados.astype(float)
    arquivo_transposto_csv = arquivo_original_csv.T
    lista_dados_chuva = [i1[i2] for i1 in arquivo_transposto_csv for i2 in range(0,12)]
    lista_bacia = [item]*528
    data_chuva_cfs_global = {'Bacia': lista_bacia, 'Ano':lista_anos, 'Mes':lista_meses, 'Precipitacao': lista_dados_chuva}
    df_temp = pd.DataFrame(data_chuva_cfs_global)
    df_dados_fornecidos_global = df_dados_fornecidos_global.append(df_temp)

df_dados_fornecidos_global.to_csv('resumo_cfs_fornecido.csv', index = False, header = True) 