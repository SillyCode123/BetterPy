def format(build):
    buildLines = build.splitlines()
    
    tabs =0
    curTabs = ""
    formated = ""
    for curS in buildLines:
        curTabs = ""
        
        for _ in range(0, tabs):
            curTabs += "    "
            
        cur = ""
        
        if "{" in curS:
            formated += "\n"
            tabs += 1
            cur = curS.replace("{", ":")
        
        elif "}" in curS:
            tabs -= 1
            cur = curS.replace("}", "")
            
        elif curS:
            cur = curS 
    
        if curS:
            formated += curTabs + cur.strip() + "\n"    
 
    return formated.strip()