# 🚀 Sistema de Processamento de Dados de Sensores

Sistema web para processamento e visualização de dados de sensores térmicos com backend Flask e frontend HTML/JavaScript.

## 📋 Características

- ✅ Processamento de até 200 sensores simultaneamente
- ✅ Suporte a 10.000+ registros por sensor
- ✅ Gráficos interativos com Chart.js
- ✅ Exportação para PDF e Excel
- ✅ Backend Flask para processamento eficiente
- ✅ Interface responsiva e intuitiva

## 🛠️ Tecnologias

**Backend:**
- Python 3.11
- Flask 3.0
- Flask-CORS 4.0
- Gunicorn (produção)

**Frontend:**
- HTML5 / CSS3 / JavaScript
- Chart.js 3.7
- jsPDF
- SheetJS (xlsx)

## 🚀 Deploy no Railway

### **Passo 1: Criar Repositório no GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPO.git
git push -u origin main
```

### **Passo 2: Deploy no Railway**

1. Acesse: https://railway.app/
2. Faça login com GitHub
3. Clique em "New Project"
4. Selecione "Deploy from GitHub repo"
5. Escolha seu repositório
6. Railway detectará automaticamente o Python e fará deploy!

### **Passo 3: Configurar Domínio**

1. No Railway, vá em "Settings"
2. Em "Domains", clique em "Generate Domain"
3. Copie a URL gerada (ex: `seu-app.up.railway.app`)
4. Pronto! Acesse a URL no navegador

## 💻 Desenvolvimento Local

### **Requisitos:**
- Python 3.11+
- pip

### **Instalação:**

```bash
# Clonar repositório
git clone https://github.com/SEU-USUARIO/SEU-REPO.git
cd SEU-REPO

# Instalar dependências
pip install -r requirements.txt

# Iniciar servidor
python sensor_data_server.py
```

### **Uso:**

1. Abra `index.html` no navegador
2. Cole os dados dos sensores
3. Configure os parâmetros
4. Clique em "Gerar Gráficos"
5. Visualize e exporte resultados

## 📁 Estrutura do Projeto

```
├── sensor_data_server.py      # Servidor Flask (backend)
├── index.html                  # Interface web (frontend)
├── requirements.txt            # Dependências Python
├── Procfile                    # Configuração Railway/Heroku
├── runtime.txt                 # Versão do Python
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo
```

## 🔧 Configuração

### **Variáveis de Ambiente:**

- `PORT` - Porta do servidor (padrão: 5000)

### **URLs:**

- **Local:** `http://localhost:5000`
- **Produção:** Detectado automaticamente

## 📊 API Endpoints

### **GET /api/health**
Verifica status do servidor

**Resposta:**
```json
{
  "status": "ok",
  "message": "Servidor Flask funcionando!"
}
```

### **POST /api/process-sensors**
Processa dados de sensores

**Request:**
```json
{
  "sensors": [
    {
      "id": "sensor1",
      "sensorId": "DLH-176",
      "data": "2025-01-01 10:00:00|25.5|60.2\n..."
    }
  ],
  "dataType": "temp",
  "dateFormat": "english",
  "allDates": true,
  "startDate": null,
  "endDate": null
}
```

**Response:**
```json
{
  "timestamps": [1704106800000, ...],
  "dataPoints": {
    "1704106800000": {
      "sensor1": 25.5
    }
  },
  "totalPoints": 1000,
  "totalSensors": 2
}
```

## 🎯 Funcionalidades

### **Processamento de Dados:**
- Parse de múltiplos formatos de data
- Sincronização de timestamps
- Filtros de data personalizados
- Suporte a temperatura e umidade

### **Visualização:**
- Gráficos de linha interativos
- Tabelas com estatísticas
- Identificação de pontos frios/quentes
- Colorização por especificação

### **Exportação:**
- PDF com gráficos e tabelas
- Excel com dados brutos
- Upload de croqui opcional

## 🚨 Solução de Problemas

### **Erro: "Servidor Flask não está rodando"**
- Certifique-se de que o servidor está iniciado
- Verifique se a porta 5000 está livre
- Em produção, aguarde o deploy completar

### **Erro: "Não foram encontrados dados válidos"**
- Verifique o formato dos dados (Data|Temp|Umidade)
- Confirme o formato de data selecionado
- Certifique-se de que há dados nos campos

### **Erro de memória (local)**
- Use a versão com servidor (esta!)
- Processe em lotes menores
- Use filtros de data

## 📝 Formato dos Dados

**Temperatura:**
```
2025-01-01 10:00:00|25.5
2025-01-01 10:01:00|25.6
```

**Temperatura e Umidade:**
```
2025-01-01 10:00:00|25.5|60.2
2025-01-01 10:01:00|25.6|60.1
```

**Formatos de data suportados:**
- Inglês: `YYYY-MM-DD HH:MM:SS`
- Português: `DD-MM-YY HH:MM:SS`

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📄 Licença

Este projeto é de código aberto para uso pessoal e comercial.

## 👤 Autor

Desenvolvido para resolver problemas de memória ao processar grandes volumes de dados de sensores.

## 🙏 Agradecimentos

- Chart.js pela biblioteca de gráficos
- Flask pela framework web
- Railway pela plataforma de deploy

---

**Deploy fácil no Railway em 3 cliques! 🚀**

