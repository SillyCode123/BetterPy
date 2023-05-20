#build ist ein string
def build(filecontent):
    # Extract function definitions
    fns = filecontent[filecontent.find("fn"): filecontent.rfind("}") + 1]
    filecontent = filecontent.replace(fns, "")
    filecontent = fns + "" + filecontent
    
    filecontents = filecontent.splitlines()
    for i in filecontents:
        if("import" in i):
            filecontent = filecontent.replace(i,"")
            filecontent = i[i.find("import"):len(i)] + "\n" + filecontent
                
    # import to the top
    filecontent = filecontent
    
    # Replace semicolons with newlines    
    filecontent = filecontent.replace(";", "\n")
    
    # Replace "read" with "input"
    filecontent = filecontent.replace("read", "input")
    
    # Replace "fn" with "def"
    filecontent = filecontent.replace("fn", "def")
    
    # Replace "//" with "#"
    filecontent = filecontent.replace("//", "#")
    
    # Replace "true" with "True" cause py sucks
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