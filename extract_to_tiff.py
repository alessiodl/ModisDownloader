from osgeo import gdal
import os

os.environ['PROJ_LIB'] = r'C:\Users\a.dilorenzo\AppData\Local\Continuum\anaconda3\envs\geoenv\Lib\site-packages\osgeo\data\proj'
os.environ['GDAL_DATA'] = r'C:\Users\a.dilorenzo\AppData\Local\Continuum\anaconda3\envs\geoenv\Library\share'

basedir = r'downloaded_hdf'
outdir  = r'output_tiff'

# crea cartella di output se non esiste
if not os.path.exists('output_tiff'):
    os.makedirs('output_tiff')

# Pulizia preventiva della cartella di output
for img in os.listdir(outdir):
    os.remove(os.path.join(outdir,img))

HDF_list = [img for img in os.listdir(basedir)]

# Opzioni di trasformazione
translate_options = gdal.TranslateOptions(outputSRS='EPSG:4326', format = 'GTiff', creationOptions = ['COMPRESS=LZW'])

for hdf in HDF_list:
    if 'MOD11C3' in hdf:
        # Subdatasets
        LST_subds = gdal.Open(os.path.join(basedir,hdf), gdal.GA_ReadOnly).GetSubDatasets()
        LSTD = LST_subds[0][0]
        LSTN = LST_subds[5][0]
        # Esportazione in TIFF
        gdal.Translate(os.path.join(outdir, hdf[0:16]+'_0_LSTD.tiff'), LSTD, options=translate_options)
        gdal.Translate(os.path.join(outdir, hdf[0:16]+'_5_LSTN.tiff'), LSTN, options=translate_options)
    elif 'MOD13C2' in hdf:
        VI_subds  = gdal.Open(os.path.join(basedir,hdf), gdal.GA_ReadOnly).GetSubDatasets()
        NDVI = VI_subds[0][0]
        EVI  = VI_subds[1][0]
        # Esportazione in TIFF
        gdal.Translate(os.path.join(outdir, hdf[0:16]+'_0_NDVI.tiff'), NDVI, options=translate_options)
        gdal.Translate(os.path.join(outdir, hdf[0:16]+'_1_EVI.tiff'), EVI, options=translate_options)