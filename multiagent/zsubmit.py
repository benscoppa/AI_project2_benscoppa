#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Xiaomeng Wang
import pathlib as pl, os, zipfile
os.chdir(pl.Path(__file__).parent.absolute())
if not pl.Path('projectParams.py').exists() and not pl.Path('projectParams.py').is_file():
    print('Error: projectParams.py not found in the directory, make sure you put this file in the project working directory, operation aborted')
    exit(1)
else:
    import projectParams
if not pl.Path('projectParams.py').exists() and not pl.Path('projectParams.py').is_file():
    print('Error: projectParams.py not found, operation aborted')
    exit(1)
name=projectParams.PROJECT_NAME.replace(':','')
if pl.Path(f'{name}.zip').exists() and pl.Path(f'{name}.zip').is_file():
    print(f'Error: {name}.zip already exists, operation aborted')
    exit(1)
files=projectParams.STUDENT_CODE_DEFAULT.split(',')
for f in files:
    if not pl.Path(f).exists() and not pl.Path(f).is_file():
        print(f'Error: {f} not found, operation aborted')
        exit(1)
with zipfile.ZipFile(f'{name}.zip','w',zipfile.ZIP_DEFLATED) as zipf:
    for f in files:
        zipf.write(f)
        print(f'"{f}" added to {name}.zip')
print(f'\nFile {name}.zip created.\n\nPlease manually check the archive before submission, author is not responsible for any mistakes made by this script, than you!')