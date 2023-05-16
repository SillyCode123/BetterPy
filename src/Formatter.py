# build wird zum line array
def format(build):
    # das klamer zeugs
    buildLines = build.split("\n")
    
    tabs = 0
    curTabs = ""
    for i in range(0,len(buildLines)):
        if "{" in buildLines[i]  :
            tabs += 1
            buildLines[i] = buildLines[i].replace("{", ":")
        
        if "}" in buildLines[i]:
            tabs -= 1
            buildLines[i] = buildLines[i].replace("}", "")
            
        for i in range(0, tabs):
            curTabs += "    "
        
        buildLines[i] = curTabs + buildLines[i] 
    
    formated = ""
    for i in buildLines: 
        formated += i + "\n"
    
    return formated