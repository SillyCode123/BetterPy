@echo off

:: Test1
echo Test 1 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\1\Main.bpy" 
py test/1/Main.py    
echo }
echo:

:: Test2
echo Test 2 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\2\Main.bpy"
py test/2/Main.py
echo }
echo:

:: Test3
echo Test 3 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\3\Main.bpy"
echo }
echo:

:: Test3
echo Test 4 {
py src/BetterPy.py "J:\Coding\Projekts\Desktop\Python\BetterPy\test\4\Main.bpy"
py test/4/Main.py
echo }
echo:

::close
pause