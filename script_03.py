from osgeo import gdal
import os

bacias = ["bacia_do_amazonas_polygons", "bacia_do_uruguai_polygons", "bacia_do_tocantins_polygons", "bacia_do_tiete", "bacia_do_paranapanema", "bacia_do_iguacu", "bacia_do_grande"]

for item in bacias:
    print(item)
    os.system("gdalwarp -cutline /home/oem/Documents/fractal/arquivos/bacias_cfs/%s.shp -crop_to_cutline -dstalpha /home/oem/Documents/fractal/entrega/shp_prec/prec_e1_02.tif /home/oem/Documents/fractal/temp/prec_e1_cfsv2_%s.tif"%(item, item))
    os.system("gdalwarp -cutline /home/oem/Documents/fractal/arquivos/bacias_cfs/%s.shp -crop_to_cutline -dstalpha /home/oem/Documents/fractal/entrega/shp_prec/prec_e2_02.tif /home/oem/Documents/fractal/temp/prec_e2_cfsv2_%s.tif"%(item, item))
    os.system("gdalwarp -cutline /home/oem/Documents/fractal/arquivos/bacias_cfs/%s.shp -crop_to_cutline -dstalpha /home/oem/Documents/fractal/entrega/shp_prec/prec_e3_02.tif /home/oem/Documents/fractal/temp/prec_e3_cfsv2_%s.tif"%(item, item))