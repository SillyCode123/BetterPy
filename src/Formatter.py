# build wird zum line array
def format(build):
    # das klamer zeugs
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
            tabs += 1
            cur = curS.replace("{", ":")
        
        elif "}" in curS:
            tabs -= 1
            cur = curS.replace("}", "")
        
        elif curS != 0:
            cur = curS 
        
        formated += curTabs + cur.strip() + "\n"
    
    return formated[0:len(formated) - 6]