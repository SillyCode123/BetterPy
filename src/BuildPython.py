def process_string_and_integer_declarations(filecontent):
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
            value = parts[1].strip().strip(";")
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]  # Remove surrounding quotes if present
            processed_lines.append(f'{var_name} = "{value}"')
        elif line.startswith("int"):
            parts = line.split("=")
            if len(parts) != 2:
                throwError("Invalid integer declaration")
                continue
            var_name = parts[0].strip().split(" ")[1]
            value = parts[1].strip().rstrip(";")
            processed_lines.append(f'{var_name} = int({value})')
        else:
            processed_lines.append(line)

    return "\n".join(processed_lines)

def build(filecontent):
    # Process string, integer, and boolean declarations
    filecontent = process_string_and_integer_declarations(filecontent)

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
    if "/*" in filecontent and "*/" in filecontent:
        comment = filecontent[filecontent.find("/*"): filecontent.find("*/") + 2]
        commentLines = comment.splitlines(True)
        del commentLines[-1]
        recomment = ""
        for i in commentLines:
            recomment += "#" + i.replace("/*", "")

        filecontent = filecontent.replace(comment, recomment.replace("*/", ""))

    return filecontent
