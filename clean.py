import os, shutil
hdf_folder = 'downloaded_hdf'
tif_folder = 'output_tiff'

# Clean function
def delete_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Impossibile cancellare %s. Errore: %s' % (file_path, e))

# Clean data folders with clean function
delete_files(hdf_folder)
delete_files(tif_folder)
