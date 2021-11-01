from osgeo import gdal
import os
import numpy as np
import csv

bacias = ["bacia_do_amazonas_polygons", "bacia_do_uruguai_polygons", "bacia_do_tocantins_polygons", "bacia_do_tiete", "bacia_do_paranapanema", "bacia_do_iguacu", "bacia_do_grande"]

for item in bacias:
        r1 = gdal.Open('/home/oem/Documents/fractal/temp/prec_e1_cfsv2_%s.tif'%item)
        r2 = gdal.Open('/home/oem/Documents/fractal/temp/prec_e2_cfsv2_%s.tif'%item)
        r3 = gdal.Open('/home/oem/Documents/fractal/temp/prec_e3_cfsv2_%s.tif'%item)
        bands = r1.RasterCount
        print(item)
        for band in range(1, bands):
            data1 = r1.GetRasterBand(band).ReadAsArray().astype('float')
            data2 = r2.GetRasterBand(band).ReadAsArray().astype('float')
            data3 = r3.GetRasterBand(band).ReadAsArray().astype('float')
            mean1 = np.mean(data1)
            mean2 = np.mean(data2)
            mean3 = np.mean(data3)
            mean = mean1 + mean2 + mean3
            print("Band %s: Mean = %s" % (band, round(mean, 2)))
            with open('/home/oem/Documents/fractal/entrega/anomais_csfv2_gdal.csv', 'a', newline='') as csvfile:
                fieldnames = ['Bacia','Band', 'Mean']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({'Bacia':item, 'Band':band, 'Mean':mean})