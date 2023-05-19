#build ist ein string
def build(filecontent):
    # Extract function definitions
    fns = filecontent[filecontent.find("fn"): filecontent.rfind("}") + 1]
    filecontent = filecontent.replace(fns, "")
    filecontent = fns + "" + filecontent
    
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
    
    
    # If main make filecontent different
    if "main" in filecontent:
        filecontent += '\rif __name__ == "__main__"{ \n    main()'
    
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