import sys
import FileReader 
import BuildPython
import Formatter
import ErrorScan
import FileWriter

#Input path + filename 
filename = ""
if len(sys.argv) > 1:
    filename = sys.argv[1]
else: 
    filename = input("path + filename>")

# Read the given file    
read = FileReader.read(filename)
if read != False:
    #Scan the file for erros
    scanned = ErrorScan.scan(read)
    
    if scanned == True:
        # Build Python
        build = BuildPython.build(read)

        if build != False:
            # Fromat it correct
            formated = Formatter.format(build)
        
            if formated != False:
                # Write it
                FileWriter.write(formated, filename)            
    
    