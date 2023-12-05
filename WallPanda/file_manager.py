import os
import tempfile

file_paths = []

def write_temp(file_name:str,content:str)->None:
    file_desc,path= tempfile.mkstemp(suffix='-'+file_name)
    file_paths.append(path)
    with open(path,'wb') as f:
        f.write(content)
    os.close(file_desc)

def clean_temp()->None:
    for path in file_paths:
        os.remove(path)

def download():
    pass