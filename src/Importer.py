import FileReader 
import BuildPython
import Formatter
import ErrorScan
import FileWriter

def compile(filename):
    # Read the given file    
    read = FileReader.read(filename)
    if read != False:
        #Scan the file for erros
        scanned = ErrorScan.start(read, filename)
        check(read,filename)
        
        if scanned:
            # Build Python
            build = BuildPython.build(read)

            if build != False:
                # Fromat it correct
                formated = Formatter.format(build)
            
                if formated != False:
                    # Write it
                    FileWriter.write(formated, filename)
                    print('\x1b[6;30;42m' + 'Compiled ' + filename +  'Succesful!' + '\x1b[0m')
                            
    
    

def check(read, filename):
    if("import" in read ):
        readLines = read.splitlines()
        for i in readLines:
            if("import" in i and '"' in i):
                im = i[i.find('"')+1:i.rfind('"')]
                read = read.replace(i,"import " + im )
                compile(filename[0:filename.rfind("\\")] + im)
                            
    return read