@echo off
cls
echo ============================================================
echo  Iniciando Sistema de Processamento de Sensores
echo ============================================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Instale Python de: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Instalar dependencias
echo Verificando dependencias...
python -m pip install flask flask-cors --quiet --disable-pip-version-check

REM Iniciar servidor em background
echo Iniciando servidor...
start /B python sensor_data_server.py

REM Aguardar 3 segundos
timeout /t 3 /nobreak >nul

REM Abrir navegador
echo Abrindo navegador...
start "" "PL001-QUALIFICACAOTERMICAV7-COM-SERVIDOR.html"

echo.
echo ============================================================
echo  SISTEMA INICIADO!
echo ============================================================
echo.
echo  Servidor: http://localhost:5000
echo  Interface: Aberta no navegador
echo.
echo  NAO FECHE ESTA JANELA!
echo  Pressione Ctrl+C para parar o servidor
echo.
echo ============================================================
echo.

REM Manter janela aberta e mostrar logs
python sensor_data_server.py

