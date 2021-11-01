# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:07:04 2021

@author: arthur
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bacias = ["amazonia", "uruguai", "tocantins", "tiete", "paranapanema", "iguacu", "grande"]

df_chuva_base = pd.read_csv('/home/oem/Documents/fractal/entrega/resumo_cfs_fornecido.csv')
df_chuva_noaa = pd.read_csv('/home/oem/Documents/fractal/entrega/anomais_csfv2.csv')

base_anomalia = df_chuva_base[(df_chuva_base['Ano'] >= 1990) & (df_chuva_base['Ano'] <= 2020)]
base_anomalia = base_anomalia.groupby(by=['Bacia']).mean()
base_anomalia = base_anomalia.rename(columns={'Precipitacao': 'Precipitacao media 1990 - 2020'})
del base_anomalia['Ano']

base_modelo = df_chuva_base[
                            (df_chuva_base['Ano'] == 2020) & (df_chuva_base['Mes'] == 'nov') |
                            (df_chuva_base['Ano'] == 2020) & (df_chuva_base['Mes'] == 'dez') |
                            (df_chuva_base['Ano'] == 2021) & (df_chuva_base['Mes'] == 'jan') |
                            (df_chuva_base['Ano'] == 2021) & (df_chuva_base['Mes'] == 'fev') |
                            (df_chuva_base['Ano'] == 2021) & (df_chuva_base['Mes'] == 'mar') |
                            (df_chuva_base['Ano'] == 2021) & (df_chuva_base['Mes'] == 'abr')
                            ]

df_anomalia = pd.merge(base_modelo, base_anomalia,on='Bacia')
df_anomalia['Anomalia base (mm/mes)'] = df_anomalia['Precipitacao'] - df_anomalia['Precipitacao media 1990 - 2020']

df_anomalia = pd.merge(df_chuva_noaa, df_anomalia, on=['Bacia', 'Mes'])
df_anomalia['Anomalia (mm/dia)'] = df_anomalia['Anomalia (mm/dia)']*30
df_anomalia = df_anomalia.rename(columns={'Anomalia (mm/dia)': 'Anomalia CFSV2 (mm/mes)'})

sns.set_style("ticks")
sns.despine()

for bacia in bacias:
    df_plot = df_anomalia[(df_anomalia['Bacia'] == bacia)]
    index_x = df_plot['Mes'].tolist()
    index_y_base = df_plot['Anomalia base (mm/mes)'].tolist()
    index_y_csfv2 = df_plot['Anomalia CFSV2 (mm/mes)'].tolist()
    # plt.plot(index_x, index_y_base , 'r--', index_x, index_y_csfv2, 'bs')
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('Mês')
    ax1.set_ylabel('CFSV2 (mm/mês)', color=color)
    ax1.plot(index_x, index_y_csfv2, color=color, marker='^')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Base (mm/mês)', color=color)  # we already handled the x-label with ax1
    ax2.plot(index_x, index_y_base, color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title("Comparacao entre modelo NOAA e dados fornecidos - %s"%bacia)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    plt.savefig('/home/oem/Documents/fractal/entrega/figuras/comparacas_%s.png'%bacia, dpi = 300)
    plt.show()