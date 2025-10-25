#!/bin/bash

clear
echo "============================================================"
echo " Sistema de Processamento de Dados de Sensores"
echo "============================================================"
echo ""

echo "[1/4] Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python3 não encontrado!"
    echo ""
    echo "Por favor, instale Python 3.x"
    exit 1
fi
python3 --version
echo "[OK] Python encontrado!"
echo ""

echo "[2/4] Verificando dependências..."
if ! python3 -m pip show flask > /dev/null 2>&1; then
    echo "Instalando Flask e Flask-CORS..."
    python3 -m pip install flask flask-cors --quiet
    if [ $? -ne 0 ]; then
        echo "[ERRO] Falha ao instalar dependências!"
        exit 1
    fi
fi
echo "[OK] Dependências instaladas!"
echo ""

echo "[3/4] Iniciando servidor Flask..."
echo ""
echo "O servidor será iniciado em segundo plano."
echo "O navegador será aberto automaticamente."
echo ""
echo "IMPORTANTE: Mantenha este terminal aberto enquanto usar o sistema!"
echo "            Para parar o servidor, pressione Ctrl+C"
echo ""
echo "============================================================"
echo ""

# Iniciar servidor em segundo plano
python3 sensor_data_server.py &
SERVER_PID=$!

# Aguardar 3 segundos para o servidor iniciar
echo "Aguardando servidor iniciar..."
sleep 3

# Abrir o HTML no navegador padrão
echo "Abrindo interface no navegador..."
if command -v xdg-open &> /dev/null; then
    xdg-open "PL001-QUALIFICACAOTERMICAV7-COM-SERVIDOR.html" &
elif command -v open &> /dev/null; then
    open "PL001-QUALIFICACAOTERMICAV7-COM-SERVIDOR.html" &
else
    echo "Abra manualmente: PL001-QUALIFICACAOTERMICAV7-COM-SERVIDOR.html"
fi

echo ""
echo "[4/4] Sistema iniciado com sucesso!"
echo ""
echo "============================================================"
echo " SERVIDOR RODANDO (PID: $SERVER_PID)"
echo "============================================================"
echo ""
echo "  URL do servidor: http://localhost:5000"
echo "  Interface web: Aberta no navegador"
echo ""
echo "  Para PARAR o servidor: Pressione Ctrl+C"
echo ""
echo "============================================================"
echo ""

# Aguardar o servidor (mostra logs)
wait $SERVER_PID

