import os.path as path
erros = 0   # Counter for errors
file = ""   # Filename variable

def start(read, filename):
    global erros
    erros = 0
    global file
    file = filename 
    scan(read)
    
    if erros == 0:
        return True
    else:
        # Print the number of errors and the filename in red
        print("\x1b[0;30;41m"+ str(erros) + " Erros\x1b[0m " + 'in "' + file + '"')
        return False

def throwError(error, line):
    global erros
    erros += 1
    print('\x1b[0;30;41m' + 'Error:\x1b[0m in "' + file + ':' + str(line)+ '" ' + error.strip() + ".") 
    
def scan(read):
    readLines = read.splitlines()
    i = 1
    openingBracket = 0
    closingBrackets = 0
    for line in readLines:
        if("{" in line):
            openingBracket += 1
                
            if("fn" not in line and "if" not in line ):
                throwError("Need fn to declare a function or an if statement", i)     
            
            if("(" not in line and ")" not in line):
                throwError("Missing parameters", i)          
            
        if ("}" in line):
            closingBrackets += 1
            if openingBracket == 0:
               throwError("Missing opening curly bracket", i)
               
        if("import" in line and '"' in line):
            if(not path.isfile(file[0:file.rfind("\\") +1] + line[line.find('"') + 1:line.rfind('"')])):
                throwError('Not find import "' + line[line.find('"') + 1:line.rfind('"')] + '"', i)
                  
        if("(" not in line and ")" in line):
                throwError("Missing opening bracket", i)
            
        if(")" not in line and "(" in line):
            throwError("Missing closing bracket", i) 
        
        if(line.count('"') % 2 != 0):
            throwError('Missing an quote(like this => ")', i)
            
        if(line.count("'") % 2 != 0):
            throwError("Missing an quote(like this => ') ", i)
            
        # count up    
        i += 1    
        
    if(openingBracket > closingBrackets):
        throwError("Missing closing curly bracket", i)  
    
    if(openingBracket < closingBrackets):
        throwError("Missing opening curly bracket", i)     
        