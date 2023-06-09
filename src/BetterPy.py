import sys
import FileReader
import BuildPython
import Formatter
import ErrorScan
import FileWriter
import Importer

# Input path + filename
filename = ""
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("path + filename>")

# Read the given file    
read = FileReader.read(filename)
if read != False:
    # Scan the file for erros
    scanned = ErrorScan.start(read, filename)
    read = Importer.check(read, filename)

    if scanned:
        # Build Python
        build = BuildPython.build(read)

        if build != False:
            # Fromat it correct
            formated = Formatter.format(build)

            if formated != False:
                # Write it
                FileWriter.write(formated, filename)
                print('\x1b[6;30;42m' + 'Compiled ' + filename[filename.rfind("\\") + 1:len(
                    filename)] + ' Succesful!' + '\x1b[0m')
else:
    print("Non Legit File")
