@echo off
::change here to yout path (only to where your folder)
set location =J:\Coding\Projekts\Desktop\Python\
:: Test1
echo Test 1 {
py src/BetterPy.py "%location %\BetterPy\test\1\Main.bpy" 
py test/1/pyOut/Main.py    
echo }
echo:

:: Test2
echo Test 2 {
py src/BetterPy.py "%location %\BetterPy\test\2\Main.bpy"
py test/2/pyOut/Main.py
echo }
echo:


:: Test3
echo Test 3 {
py src/BetterPy.py "%location %\BetterPy\test\4\Main.bpy"
py test/3/pyOut/Main.py
echo }
echo:

:: Test4
echo Test 4{
py src/BetterPy.py "%location %\BetterPy\test\5\Main.bpy"
py test/3/pyOut/Main.py
echo }
echo:

:: Test-Error-Codes
echo Test Error Codes {
py src/BetterPy.py "%location %\BetterPy\test\Error\Main.bpy"
echo }
echo:


::close
pause