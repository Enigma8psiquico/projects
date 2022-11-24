rem @echo off
rem set /a "base = 2"
rem set /a  "potencia = 6"
rem set /a resultado=0

rem :funcion
rem set /a "resultado=%base%"
rem for /l %%i in (2 1 %potencia%) do (
rem set /a resultado = resultado * %base%
rem )
rem echo.Resultado = %resultado% 

rem pause


set /a "monto = 85"
set /a "monto = monto /8 - monto/5 - (monto/4)"

:operacion 
echo %monto%