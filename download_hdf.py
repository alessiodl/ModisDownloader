from auth import SessionWithHeaderRedirection
import requests, os
from lxml import html
import config as cfg

# Parametri
data_folder = cfg.data['yyyy.mm.dd']

# Costanti
PRODUCTS = ['MOD13C2.006', 'MOD11C3.006']
URL = 'http://e4ftl01.cr.usgs.gov/MOLT'
USERNAME = cfg.credentials['username']
PASSWORD = cfg.credentials['password']

# Autenticazione
session = SessionWithHeaderRedirection(USERNAME, PASSWORD)

# Funzione di Scaricamento de dati
def hdfDownload(url, filename):
    try:
        # submit the request using the session
        response = session.get(url, stream=True)
        # print(response.status_code)
        # raise an exception in case of http errors
        response.raise_for_status()  
        # crea cartella di download se non esiste
        if not os.path.exists('downloaded_hdf'):
            os.makedirs('downloaded_hdf')
        # save the file
        print('Salvataggio di {0} sul disco in corso...'.format(hdf_name[0]))
        with open(os.path.join('downloaded_hdf',filename), 'wb') as fd:
            for chunk in response.iter_content(chunk_size=1024*1024):
                fd.write(chunk)
        print('Operazione completata!')
    except requests.exceptions.HTTPError as e:
        # handle any errors here
        print(e)

# Ricerca e costruzione degli URL degli HDF mediante scraping
for prod in PRODUCTS:
    data_url = URL+"/"+prod+"/"+data_folder
    # print(data_url)
    resp = requests.get(data_url, auth=(USERNAME, PASSWORD))
    tree = html.fromstring(resp.content)
    links = tree.xpath('//a/text()')
    # print(links)
    subs = '.hdf'
    hdf_name = [i for i in links if subs in i]
    # print(hdf_name[0])
    hdf_url = data_url+"/"+hdf_name[0]
    # Scarica
    hdfDownload(hdf_url, hdf_name[0])
   