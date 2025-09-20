# Imagem base oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Expõe a porta Flask
EXPOSE 5000

# Define variável de ambiente para Flask
ENV FLASK_APP=app.py

# Comando padrão para rodar
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

