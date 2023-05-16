#build ist ein string
def build(filecontent):
    t = True
     
    while t:
        print("t")
        fn = filecontent[filecontent.find("fn"):filecontent.find("}") + 1]
        filecontent = filecontent.replace(fn, "")
        if "fn" not in filecontent:
            t = False
        filecontent = fn + "\n" + filecontent
        
    print(filecontent)    
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
        
    return filecontent