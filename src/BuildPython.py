#build ist ein string
def build(filecontent):
   
    fns = filecontent[filecontent.find("fn"): filecontent.rfind("}") + 1]
    filecontent = filecontent.replace(fns, "")
    filecontent = fns + "" + filecontent
        
    filecontent = filecontent.replace(";", "\n")
    filecontent = filecontent.replace("read", "input")
    filecontent = filecontent.replace("fn", "def")
    filecontent = filecontent.replace("//", "#")
    filecontent = filecontent.replace("true", "True")
    filecontent = filecontent.replace("false", "False")
    filecontent = filecontent.replace("||", "or")
    filecontent = filecontent.replace("&&", "and")    
    
    if "main" in filecontent:
        filecontent += '\rif __name__ == "__main__"{ \n    main()'
   
    if "/*" in filecontent and "*/" in filecontent:
        comment = filecontent[filecontent.find("/*"): filecontent.find("*/") + 2]
        commentLines = comment.splitlines(True)
        del commentLines[-1]
        recomment = ""
        for i in commentLines:
            recomment += "#" + i.replace("/*", "")
        
        filecontent = filecontent.replace(comment, recomment.replace("*/", ""))
    
    
        
    return filecontent