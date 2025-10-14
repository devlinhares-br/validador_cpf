# Usa imagem oficial do Python (versão leve)
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Evita que o Python gere arquivos .pyc e buffer de saída
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia o requirements.txt e instala dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que o Gunicorn vai usar
EXPOSE 8000

# Comando padrão para rodar o Gunicorn
# (ajuste o nome do módulo e app conforme sua estrutura)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
