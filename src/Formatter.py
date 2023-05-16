# build wird zum line array
def format(build):
    # das klamer zeugs
    buildLines = build.split('\n')
    
    tabs =0
    curTabs = ""
    formated = ""
    print(len(buildLines))
    for curS in buildLines:
        curTabs = ""
        for i in range(0, tabs):
            curTabs += "    "
            
        cur = ""
        
        if "{" in curS:
            tabs += 1
            cur = curS.replace("{", ":")
        
        elif "}" in curS:
            tabs -= 1
            cur = curS.replace("}", "")
        
        else:
            cur = curS 
         
        
        
        print(curS)
        formated += curTabs + cur.strip() + "\n"
     
    
    return formated