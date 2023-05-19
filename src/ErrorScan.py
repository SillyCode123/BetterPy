erros = 0
file = ""

def start(read, filename):
    global erros
    erros = 0
    global file
    file = filename 
    scan(read)
    
    if erros == 0:
        return True
    else:
        return False

def throwError(error, line):
    global erros
    erros += 1
    print('\x1b[0;30;41m' + 'Error:\x1b[0m in "' + file + '":' + str(line)+ " " + error ) 

def scan(read):
    readLines = read.splitlines()
    i = 1
    openingBracket = 0
    closingBrackets = 0
    for line in readLines:
        if("{" in line):
            openingBracket += 1
                
            if("fn" not in line and "if" not in line ):
                throwError("Need fn to declare a function or if ", i)
            
            if("(" not in line and ")" not in line):
                throwError("Missing parameters", i)
                
            elif("(" not in line):
                throwError("Missing opening bracket", i)
            
            elif(")" not in line):
                throwError("Missing closing bracket", i)    
            
        if ("}" in line):
            closingBrackets += 1
            if openingBracket == 0:
               throwError("Missing opening curly bracket", i)
                  
        i += 1
    
        
    if(openingBracket > closingBrackets):
        throwError("Missing closing curly bracket", i)  
    
    if(openingBracket < closingBrackets):
        throwError("Missing opening curly bracket", i)     
        
    
  
    