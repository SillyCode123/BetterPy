import os

def write(content, filename):
    path = filename[0:filename.rfind("\\")+1] + "pyOut\\"
    if(not os.path.isdir(path)):
        os.mkdir(path)
        

    with open(path + filename[filename.rfind("\\")+1: filename.rfind(".")] + ".py" , "w") as file:
        file.write(content)
    