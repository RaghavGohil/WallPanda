import os
import tempfile
import gui

file_paths = []

gui_instance = None 

def set_gui_instance(instance):
    global gui_instance
    gui_instance = instance

def write_temp(file_name:str,content:str)->None:
    file_desc,path= tempfile.mkstemp(suffix='-'+file_name)
    file_paths.append(path)
    with open(path,'wb') as f:
        f.write(content)
    os.close(file_desc)
    gui_instance.create_button(path)

def cleanup()->None:
    for path in file_paths:
        os.remove(path)

def download():
    pass