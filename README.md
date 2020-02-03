# ModisDownloader
Collezione di script Python per lo scarico e l'estrazione in formato TIFF dei dati MODIS per i prodotti MOD11C3 e MOD13C2.

## Utilizzo
  * Creare un file **config.py** in cui siano definite, in formato json, le credenziali di accesso al servizio e i limiti temporali dei dati MODIS da scaricare. Es:
```
credentials = {
    'username': 'myUsername', 
    'password': 'myPassword!'
}

data = {
    'year':'2015',
    'months': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
}
```
  * Lanciare lo script *download_hdf.py*
  * Lanciare lo script *extract_to_tiff.py*
  
<img src="screenshot.png" />
