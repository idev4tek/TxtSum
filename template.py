import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ='TxtSum'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb'
]

# createe the Directories and Files
for file in list_of_files:
    fldr, filename = os.path.split(file)

    # create directory doesnt exist
    if fldr != '':
        os.makedirs(fldr,exist_ok=True) 
        logging.info('foler: {fldr}  has been created')

    # Create empty file 
    if (not os.path.exists(file)) or (os.path.getsize(file)):
        with open(file,'w') as f:
            pass
        logging.info(f'create empty file {file}')
    else:
        logging.info(f'File {file} already exists')