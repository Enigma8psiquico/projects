:: Cuenta del 1 al 5000
FOR /L %%G IN (1,1,5000) DO echo %%G 
Pause 

:: Las listas no numéricas pueden usar un comando FOR estándar:
FOR %%G IN (Sun Mon Tues Wednes Thurs Fri Satur) DO echo %%Gday              
Pause          


@echo off  
prompt "::"
color 6
SET /A "ola=0"
PAUSE
SET "%ola%=%ola%+1"

PAUSE
if '%ola%' == '10'(
PAUSE
start https://www.youtube.com/shorts/vly72GM0yKg
echo BB   BB    BB    BB  BB  BBBBBBB BBBBBB 
ECHO BB   BB   BB BB  BB BB   BB      BB   BB 
ECHO BBBBBBB  BB  BB  BBB     BBBB    BB   BB 
ECHO BB   BB  BBBBBB  BB BB   BB      BB   BB 
ECHO BB   BB BB    BB BB   BB BBBBBBB BBBBBB 
echo.
echo.
ECHO Hola Leo XD
echo.
echo.
PAUSE     
)
