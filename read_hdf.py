from osgeo import gdal
import os

basedir = r'downloaded_hdf'
outdir = r'output_tiff'

# crea cartella di output se non esiste
if not os.path.exists('output_tiff'):
    os.makedirs('output_tiff')

MODIS_files = [img for img in os.listdir(basedir)]

MOD11C3 = MODIS_files[0]
MOD13C2 = MODIS_files[1]

# Subdatasets
sds_lst = gdal.Open(os.path.join(basedir,MOD11C3), gdal.GA_ReadOnly).GetSubDatasets()
sds_vi  = gdal.Open(os.path.join(basedir,MOD13C2), gdal.GA_ReadOnly).GetSubDatasets()

'''
print (sds_lst[0])
print (sds_lst[5])
print (sds_vi[0])
print (sds_vi[1])
'''

lst_day = sds_lst[0][0]
lst_night = sds_lst[5][0]
ndvi = sds_vi[0][0]
evi = sds_vi[1][0]

'''
print(lst_day)
print(lst_night)
print(ndvi)
print(evi)
'''
# Pulizia della cartella di output
for img in os.listdir(outdir):
    os.remove(os.path.join(outdir,img))

# ################################
# ESPORTAZIONE DEI DATASET IN TIFF
# ################################

# Compressione
translate_options = gdal.TranslateOptions(outputSRS='EPSG:4326', format = 'GTiff', creationOptions = ['COMPRESS=LZW'])
# Esportazione in TIFF
gdal.Translate(os.path.join(outdir, MOD11C3[0:16]+'_0_LSTD.tiff'), lst_day, options=translate_options)
gdal.Translate(os.path.join(outdir, MOD11C3[0:16]+'_5_LSTN.tiff'), lst_night, options=translate_options)
gdal.Translate(os.path.join(outdir, MOD13C2[0:16]+'_0_NDVI.tiff'), ndvi, options=translate_options)
gdal.Translate(os.path.join(outdir, MOD13C2[0:16]+'_1_EVI.tiff'), evi, options=translate_options)