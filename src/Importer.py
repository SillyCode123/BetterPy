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
                    print('Compiled ' + filename +  ' Succesful!')
                            
    
    

def check(read, filename):
    if("import" in read ):
        readLines = read.splitlines()
        for i in readLines:
            if("import" in i and '"' in i):
                im = i[i.find('"')+1:i.rfind('"')]
                read = read.replace(i,"")
                read = "import " + im[0:im.rfind(".")] + "\n" + read
                compile(filename[0:filename.rfind("\\") + 1] + "" + im)
                            
    return read