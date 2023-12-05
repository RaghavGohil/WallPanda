import os
import tempfile

all_file_paths = []
image_stack = []

def write_temp(file_name:str,content:str)->None:
    file_desc,path= tempfile.mkstemp(suffix='-'+file_name)
    all_file_paths.append(path)
    image_stack.append(path)
    with open(path,'wb') as f:
        f.write(content)
    os.close(file_desc)

def clean_temp()->None:
    for path in all_file_paths:
        os.remove(path.replace('\\\\','/'))
    all_file_paths.clear()

def download():
    pass