from ErrorScan import throwError

def build(filecontent):
    # Extract function definitions
    fns = filecontent[filecontent.find("fn"): filecontent.rfind("}") + 1]
    filecontent = filecontent.replace(fns, "")
    filecontent = fns + "" + filecontent

    filecontents = filecontent.splitlines()

    # Imports
    filecontents = filecontent.splitlines()
    for i in filecontents:
        if("import" in i):
            filecontent = filecontent.replace(i,"")
            filecontent = i[i.find("import"):len(i)] + "\n" + filecontent

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
    
    filecontent = filecontent.replace("String", "TEST")

    # Convert /* ... */ comments to # comments
    if "/*" in filecontent and "*/" in filecontent:
        comment = filecontent[filecontent.find("/*"): filecontent.find("*/") + 2]
        commentLines = comment.splitlines(True)
        del commentLines[-1]
        recomment = ""
        for i in commentLines:
            recomment += "#" + i.replace("/*", "")

        filecontent = filecontent.replace(comment, recomment.replace("*/", ""))

    # Process each line
    processed_lines = []
    for line in filecontents:
        processed_line = processStringDeclaration(line)
        if processed_line is not None:
            processed_lines.append(processed_line)
        else:
            processed_lines.append(line)

    # Join the lines back into a single string
    filecontent = "\n".join(processed_lines)

    return filecontent

def processStringDeclaration(line):
    line = line.strip()
    if line.startswith("String"):
        parts = line.split("=")
        if len(parts) != 2:
            throwError("Invalid string declaration")
            return None
        varName = parts[0].strip().split(" ")[1]
        value = parts[1].strip()
        return f'{varName} = "{value}"'
    return line
