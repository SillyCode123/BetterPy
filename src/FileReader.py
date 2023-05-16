import os.path as file

def read(filename):
    if file.isfile(filename) != True:
        print("Non Legit File")
        return False
    
    return open(filename).read()
    
            