#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:04:12 2021

@author: oem
"""

from osgeo import gdal
gdal.AllRegister()
rast_src = gdal.Open('/home/oem/Documents/fractal/arquivos/teste_exportacao/prec_e2_v03.tif', 1 )
gt = rast_src.GetGeoTransform()
gtl = list(gt)
gtl[0] -= 360
gtl[3] -= 0
rast_src.SetGeoTransform(tuple(gtl))
rast_src = None