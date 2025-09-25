# 🐳 Ngrok-Manage (Gerenciamento de Túnel Ngrok com Docker)

Este repositório é um projeto demo para quem quer aprender sobre Docker e, principalmente, gerenciar túneis Ngrok de forma eficiente. A aplicação, construída com Flask e Python, oferece uma interface web que permite criar, monitorar e controlar túneis Ngrok, todos rodando dentro de um contêiner Docker.

O objetivo principal deste projeto é gerenciamento de túneis Ngrok. Além disso, você vai aprender a:

- Criar um Dockerfile para empacotar uma aplicação Python.
- Construir e rodar um contêiner Docker.
- Mapear portas e usar volumes (-v) para persistir dados de configuração do Ngrok.

🛠️ Aplicação de Exemplo

A aplicação fornece uma interface web simples para:

- Iniciar novos túneis Ngrok (HTTP/HTTPS).
- Monitorar túneis ativos e seus URLs públicos.
- Parar ou reiniciar túneis existentes.

A interface facilita o gerenciamento de túneis sem depender do terminal.

📁 Estrutura do Projeto
```
Ngrok-Manage/
│
├── app.py                # Lógica principal da aplicação Flask
├── templates/
│   └── index.html        # Template HTML da página inicial
├── static/
│   └── style.css         # CSS opcional para estilização
├── ngrok_config.json     # Configuração padrão opcional dos túneis Ngrok
├── requirements.txt      # Dependências Python (Flask)
└── Dockerfile            # Instruções para construir a imagem Docker
```
🚀 Como Usar e Aprender

1. Construir a Imagem Docker

    Abra o terminal na raiz do projeto e execute:

`docker build -t ngrok-manage:1.0` .

2. Preparar uma Pasta de Configuração

    Crie uma pasta local para armazenar logs e configurações do Ngrok:

    `mkdir ~/ngrok_data`

    Coloque quaisquer arquivos de configuração .json do Ngrok nessa pasta, se necessário.

3. Rodar o Contêiner

    Execute o contêiner, conectando a pasta criada:

    ```
    docker run -d \
      -p 5000:5000 \
      -v ~/ngrok_data:/root/ngrok_data \
      --name ngrok-manage \
      ngrok-manage:1.0
    ```
    Explicação dos parâmetros:

    - `-d`: Executa o contêiner em segundo plano.
    - `-p 5000:5000`: Mapeia a porta 5000 da sua máquina para a porta 5000 do contêiner.
    - `-v ~/ngrok_data:/root/ngrok_data`: Conecta a pasta local à pasta do contêiner, persistindo os dados.
    - `--name ngrok-manage`: Dá um nome fácil de usar ao contêiner.

4. Acessar a Aplicação

    Abra o navegador em:

    `http://localhost:5000`

    Você verá a interface de gerenciamento dos túneis Ngrok. Crie, monitore ou pare túneis. Mudanças nos arquivos de configuração na pasta local são refletidas imediatamente na aplicação.

    📦 Variáveis de Ambiente (.env)

    Para facilitar a configuração, você pode criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    POST_URL=<url-api>
    POST_ID=<id>
    NGROK_AUTHTOKEN=<token-ngrok>
    AUTH_API=<token-api>
    ```

    - **POST_URL**: URL que receberá requisições POST da aplicação.
    - **POST_ID**: ID usado para identificar o POST.
    - **NGROK_AUTHTOKEN**: Token de autenticação do Ngrok.
    - **AUTH_API**: Chave de autenticação da API interna.

    Coloque essas variáveis no `.env` e certifique-se de que o Flask esteja configurado para ler essas variáveis ao iniciar a aplicação.

🤝 Contribuindo

Sinta-se à vontade para usar este projeto como base para gerenciar túneis Ngrok e aprender Docker/Flask. Sugestões ou melhorias podem ser enviadas via issue ou pull request.
