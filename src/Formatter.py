def format(build):
    # split the build string into lines
    buildLines = build.splitlines()
    
    tabs =0    # keep track of current indent level
    curTabs = ""    # store current indentation spaces
    formated = ""   # string to store formated code
    
    # go through each line in the build string
    for curS in buildLines:
        curTabs = "" # reset intendation level
        
        # add the right number of indentation spaces
        for _ in range(0, tabs):
            curTabs += "    "
            
        cur = ""    # stores modified line
        
        # check for open curly brackets
        if "{" in curS:
            tabs += 1   # increase intendation level
            cur = curS.replace("{", ":")    # replace "{" with ":"
        
        # Check for closed curly brackets
        elif "}" in curS:
            tabs -= 1
            cur = curS.replace("}", "") # replace "}" with nothing
            
        # else set the line to the line
        elif curS:
            cur = curS 
    
        if curS:
            # Add the formatted line with the right indentation to get the final result
            formated += curTabs + cur.strip() + "\n"    
 
    return formated.strip()