import os.path as file

def read(filename):
    if not file.isfile(filename):
        print("Non Legit File")
        return False
    
    with open(filename) as f:
        return f.read()
    
            