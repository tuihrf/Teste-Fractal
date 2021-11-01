#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:20:06 2021

@author: oem
"""

import requests


#entrar com a data no formato AAAAMMDD
def download_noaa(data):
    horarios = ['00', '06', '12', '18']
    for horaa in horarios:
        url = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_cfs_flx.pl?file=flxf{0}{1}.01.{0}{1}.grb2&all_lev=on&all_var=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fcfs.{0}%2F{1}%2F6hrly_grib_01'.format(data, horaa)
        requisicao = requests.get(url)
        if requisicao.status_code == 200:
            open('grib2_downloads/%s_%s.grb2'%(data, horaa), 'wb').write(requisicao.content)
            print("GRIB2 %s - %s OK"%(data, horaa))
        else:
            print("GRIB2 %s - %s FALHOU"%(data, horaa))

#Exemplo de execução:
# download_noaa("20211101")

# Retorno esperado:
# GRIB2 20211101 - 00 OK
# GRIB2 20211101 - 06 OK
# GRIB2 20211101 - 12 FALHOU
# GRIB2 20211101 - 18 FALHOU