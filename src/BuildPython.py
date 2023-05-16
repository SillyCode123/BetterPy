#build ist ein string
def build(filecontent):
    filecontent = filecontent.replace(";", "\n")
    filecontent = filecontent.replace("read", "input")
    filecontent = filecontent.replace("fn", "def")
    filecontent = filecontent.replace("//", "#")
    filecontent = filecontent.replace("#", "//")
    filecontent = filecontent.replace("/*", '"""')
    filecontent = filecontent.replace("true", "True")
    filecontent = filecontent.replace("false", "False")
    
    return filecontent