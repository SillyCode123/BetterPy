#build ist ein string
def build(filecontent):
   
    fns = filecontent[filecontent.find("fn"): filecontent.rfind("}") + 1]
    filecontent = filecontent.replace(fns, "")
    filecontent = fns + "" + filecontent
        
    filecontent = filecontent.replace(";", "\n")
    filecontent = filecontent.replace("read", "input")
    filecontent = filecontent.replace("fn", "def")
    filecontent = filecontent.replace("//", "#")
    filecontent = filecontent.replace("#", "//")
    filecontent = filecontent.replace("/*", '"""')
    filecontent = filecontent.replace("true", "True")
    filecontent = filecontent.replace("false", "False")
    filecontent = filecontent.replace("||", "or")
    filecontent = filecontent.replace("&&", "and")    
    
    if "main" in filecontent:
        filecontent += '\rif __name__ == "__main__"{ \n    main()'
        
    return filecontent