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
        read = check(read,filename)
        if scanned:
            # Build Python
            build = BuildPython.build(read)

            if build != False:
                # Fromat it correct
                formated = Formatter.format(build)
            
                if formated != False:
                    # Write it
                    FileWriter.write(formated, filename)
                    print('\x1b[6;30;42m' + 'Compiled ' + filename +  ' Succesful!' + '\x1b[0m')
                            
    
    

def check(read, filename):
    if("import" in read ):
        readLines = read.splitlines()
        for i in readLines:
            if("import" in i and '"' in i):
                im = i[i.find('"')+1:len(i)].replace('"', "")
                read = read.replace(i,"")
                read = "import " + im[0:im.rfind(".")] + im[im.rfind(".") + 4: len(im)] + "\n" + read
                compile(filename[0:filename.rfind("\\") + 1] + "" + i[i.find('"') +1:i.rfind('"')])
                            
    return read