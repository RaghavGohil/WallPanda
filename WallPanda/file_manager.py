import os
import tempfile

file_paths = []

def write_temp(file_name:str,content:str):
    file_desc,path= tempfile.mkstemp(suffix='-'+file_name)
    print(path)
    with open(path,'wb') as f:
        f.write(content)
    os.close(file_desc)

def cleanup():
    for path in file_paths:
        os.remove(path)

def download():
    pass