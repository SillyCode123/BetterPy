import os

def write(content, filename):
    file_path = os.path.splitext(filename)[0] + ".py"
    
    with open(file_path, "w") as file:
        file.write(content)