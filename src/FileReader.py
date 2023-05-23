import os.path as file

def read(filename):
    if not file.isfile(filename):
        return False
    
    with open(filename) as f:
        return f.read()
    
            