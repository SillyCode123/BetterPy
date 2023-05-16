import os.path as file

def write(content, filename):
    if file.exists(filename.split(".")[0] + ".py"):
         open(filename.split(".")[0] + ".py", "w").write(content)
    else :
        open(filename.split(".")[0] + ".py" , "x").write(content)

    