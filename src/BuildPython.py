def build(filecontent):
    # Extract function definitions
    fns = filecontent[filecontent.find("fn"): filecontent.rfind("}") + 1]
    filecontent = filecontent.replace(fns, "")
    filecontent = fns + "" + filecontent

    filecontents = filecontent.splitlines()

    # Import
    imports = []
    new_filecontent = []
    for line in filecontents:
        if "import" in line:
            imports.append(line)
        else:
            new_filecontent.append(line)

    filecontent = "\n".join(imports) + "\n" + "\n".join(new_filecontent)

    # Replace semicolons with newlines
    filecontent = filecontent.replace(";", "\n")

    # Replace "read" with "input"
    filecontent = filecontent.replace("read", "input")

    # Replace "fn" with "def"
    filecontent = filecontent.replace("fn", "def")

    # Replace "//" with "#"
    filecontent = filecontent.replace("//", "#")

    # Replace "true" with "True"
    filecontent = filecontent.replace("true", "True")
    
     # Replace "false" with "False"
    filecontent = filecontent.replace("false", "False")

    # Replace "||" with "or"
    filecontent = filecontent.replace("||", "or")

    # Replace "&&" with "and"
    filecontent = filecontent.replace("&&", "and")

    # Convert /* ... */ comments to # comments
    while "/*" in filecontent and "*/" in filecontent:
        start = filecontent.find("/*")
        end = filecontent.find("*/") + 2
        comment = filecontent[start:end]
        filecontent = filecontent.replace(comment, comment.replace("/*", "#").replace("*/", ""))

    return filecontent