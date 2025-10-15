# Use uma imagem base do Python oficial
FROM python:3.9-slim

# Instala as dependências do sistema necessárias para o Chrome Headless
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    --no-install-recommends

# Baixa e instala a versão estável mais recente do Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    --no-install-recommends \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências e instala as bibliotecas Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da sua aplicação para o contêiner
COPY . .

# Comando padrão para executar quando o serviço iniciar (será sobrescrito no Render)
# Deixamos um comando padrão aqui para o caso de testes locais
CMD ["python", "consulta_placa.py"]
