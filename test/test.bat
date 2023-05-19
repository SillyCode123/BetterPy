@echo off

:: Test1
echo Test1 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\1\Main.bpy" 
py test/1/Main.py    
echo }
echo:

:: Test2
echo Test2 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\2\Main.bpy"
py test/2/Main.py
echo }
echo:

:: Test3
echo Test3 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\3\Main.bpy"
py test/3/Main.py
echo }
echo:

::close
pause