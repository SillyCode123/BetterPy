@echo off
cd ..
::change here to yout path (only to where your folder)
set location =E:\Coding\Desktop\Python\BetterPy

:: Test1
echo Test 1 {
py src/BetterPy.py "%location %\test\1\Main.bpy"
py test/1/pyOut/Main.py    
echo }
echo:

:: Test2
echo Test 2 {
py src/BetterPy.py "%location %\test\2\Main.bpy"
py test/2/pyOut/Main.py
echo }
echo:


:: Test3
echo Test 3 {
py src/BetterPy.py "%location %\test\4\Main.bpy"
py test/3/pyOut/Main.py
echo }
echo:

:: Test4
echo Test 4{
py src/BetterPy.py "%location %\test\5\Main.bpy"
py test/3/pyOut/Main.py
echo }
echo:

:: Test-Error-Codes
echo Test Error Codes {
py src/BetterPy.py "%location %\test\Error\Main.bpy"
echo }
echo:

::close
pause