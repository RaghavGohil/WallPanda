import tempfile

def write_temp(file_name:str,content:str):
    temp = tempfile.NamedTemporaryFile(mode='wb',suffix='-'+file_name)
    print(temp.name)
    temp.write(content)
    temp.close()

def download():
    pass