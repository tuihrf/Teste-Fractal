# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:07:04 2021

@author: arthur
"""
import pandas as pd

df_chuva_base = pd.read_csv('/home/oem/Documents/fractal/entrega/resumo_cfs_fornecido.csv')
df_chuva_noaa = pd.read_csv('/home/oem/Documents/fractal/entrega/anomais_csfv2_gdal.csv', header = None)

df_chuva_noaa = df_chuva_noaa.rename(columns={0: 'Bacia', 1: 'Band', 2: 'Anomalia (mm/dia)'})

df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_amazonas_polygons'],'amazonia')
df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_uruguai_polygons'],'uruguai')
df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_tocantins_polygons'],'tocantins')
df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_tiete'],'tiete')
df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_paranapanema'],'paranapanema')
df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_iguacu'],'iguacu')
df_chuva_noaa['Bacia'] = df_chuva_noaa['Bacia'].replace(['bacia_do_grande'],'grande')

df_chuva_noaa['Band'] = df_chuva_noaa['Band'].replace([1],'nov')
df_chuva_noaa['Band'] = df_chuva_noaa['Band'].replace([2],'dez')
df_chuva_noaa['Band'] = df_chuva_noaa['Band'].replace([3],'jan')
df_chuva_noaa['Band'] = df_chuva_noaa['Band'].replace([4],'fev')
df_chuva_noaa['Band'] = df_chuva_noaa['Band'].replace([5],'mar')
df_chuva_noaa['Band'] = df_chuva_noaa['Band'].replace([6],'abr')

df_chuva_noaa = df_chuva_noaa.rename(columns={'Band': 'Mes'})

df_chuva_noaa.to_csv('anomais_csfv2.csv', index = False, header = True) 