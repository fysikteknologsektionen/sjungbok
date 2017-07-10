@echo off
pdflatex.exe framsida.tex
echo Klar!
pause
del framsida.aux
del framsida.log
