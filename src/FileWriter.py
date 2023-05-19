import os.path as file

def write(content, filename):
    # Check if file python already exists
    if file.exists(filename.split(".")[0] + ".py"):
        # Overwrite it's content
         open(filename.split(".")[0] + ".py", "w").write(content)
    else :
        # Create new python file
        open(filename.split(".")[0] + ".py" , "x").write(content)

    