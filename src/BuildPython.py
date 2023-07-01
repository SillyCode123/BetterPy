def build(filecontent):

    filecontent = process_string_integer(filecontent)

    # Impor
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
<<<<<<< HEAD
=======
    
    # Replace "int" with "nothing"
    filecontent = filecontent.replace("int ", "")
    
    filecontent = filecontent.replace("String ", " ")
<<<<<<< HEAD
>>>>>>> parent of 5bb1a76 (Should work)
=======
>>>>>>> parent of 5bb1a76 (Should work)

    # Convert /* ... */ comments to # comments
    if "/*" in filecontent and "*/" in filecontent:
        comment = filecontent[filecontent.find("/*"): filecontent.find("*/") + 2]
        commentLines = comment.splitlines(True)
        del commentLines[-1]
        recomment = ""
        for i in commentLines:
            recomment += "#" + i.replace("/*", "")

        filecontent = filecontent.replace(comment, recomment.replace("*/", ""))

<<<<<<< HEAD
<<<<<<< HEAD
    # Join the lines back into a single string
    filecontent = "\n".join(processed_lines)

    return filecontent

def process_string_integer(filecontent):
    lines = filecontent.splitlines()
    processed_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("String"):
            parts = line.split("=")
            if len(parts) != 2:
                throwError("Invalid string declaration")
                continue
            var_name = parts[0].strip().split(" ")[1]
            value = parts[1].strip().strip(";").strip('"')
            processed_lines.append(f'{var_name} = "{value}"')
        elif line.startswith("int"):
            parts = line.split("=")
            if len(parts) != 2:
                throwError("Invalid integer declaration")
                continue
            var_name = parts[0].strip().split(" ")[1]
            value = parts[1].strip().rstrip(";")
            processed_lines.append(f'{var_name} = int({value})')
        elif line.startswith("Boolean"):
            parts = line.split("=")
            if len(parts) != 2:
                throwError("Invalid boolean declaration")
                continue
            var_name = parts[0].strip().split(" ")[1]
            value = parts[1].strip().rstrip(";")
            processed_lines.append(f'{var_name} = bool({value})')
        else:
            processed_lines.append(line)

    return "\n".join(processed_lines)
=======

    return filecontent
>>>>>>> parent of 5bb1a76 (Should work)
=======

    return filecontent
>>>>>>> parent of 5bb1a76 (Should work)
