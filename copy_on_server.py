import os
import config as cfg
import shutil

srv = cfg.server['path']
year = cfg.data['year']

server_path = os.path.join(srv,year)

for tiff_file in os.listdir('output_tiff'):
    print('Copying {}'.format(tiff_file))
    shutil.copy(os.path.join('output_tiff', tiff_file), os.path.join(server_path, tiff_file))

print("Copy complete")