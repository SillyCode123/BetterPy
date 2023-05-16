import sys
import FileReader 
import BuildPython
import Formatter
import FileWriter

filename = ""


if len(sys.argv) > 1:
    filename = sys.argv[1]
else: 
    filename = input("filename>")
    
read = FileReader.read(filename)
 
if read != False:
    build = BuildPython.build(read)

    if build != False:
        formated = Formatter.format(build)
        
        if formated != False:
            FileWriter.write(formated)            
    
    