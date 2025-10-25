@echo off
chcp 65001 >nul 2>&1
cls
echo ============================================================
echo  Sistema de Processamento de Dados de Sensores
echo ============================================================
echo.

echo [1/4] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale Python 3.x de:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)
python --version
echo [OK] Python encontrado!
echo.

echo [2/4] Verificando dependencias...
python -m pip show flask >nul 2>&1
if errorlevel 1 (
    echo Instalando Flask e Flask-CORS...
    python -m pip install flask flask-cors
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias!
        pause
        exit /b 1
    )
)
echo [OK] Dependencias instaladas!
echo.

echo [3/4] Iniciando servidor Flask...
echo.
echo O servidor sera iniciado em segundo plano.
echo Uma nova janela do navegador sera aberta automaticamente.
echo.
echo IMPORTANTE: NAO FECHE ESTA JANELA enquanto usar o sistema!
echo             Para parar o servidor, feche esta janela.
echo.
echo ============================================================
echo.

echo Aguardando servidor iniciar...
start /B python sensor_data_server.py
timeout /t 3 /nobreak >nul

echo Abrindo interface no navegador...
start "" "PL001-QUALIFICACAOTERMICAV7-COM-SERVIDOR.html"

echo.
echo [4/4] Sistema iniciado com sucesso!
echo.
echo ============================================================
echo  SERVIDOR RODANDO
echo ============================================================
echo.
echo  URL do servidor: http://localhost:5000
echo  Interface web: Aberta no navegador
echo.
echo  Para PARAR o servidor: Feche esta janela ou pressione Ctrl+C
echo.
echo ============================================================
echo.

python sensor_data_server.py

