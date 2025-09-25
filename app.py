import os
import requests
from flask import Flask, request, render_template
from pyngrok import ngrok
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)
current_tunnel = None

POST_URL = os.getenv("POST_URL")
POST_ID = int(os.getenv("POST_ID", 1))
AUTH_API = os.getenv("AUTH_API", 1) 

@app.route("/", methods=["GET", "POST"])
def index():
    global current_tunnel
    url = None
    if request.method == "POST":
        porta = int(request.form["porta"])
        if current_tunnel:
            ngrok.disconnect(current_tunnel.public_url)
        current_tunnel = ngrok.connect(porta, "http")
        url = current_tunnel.public_url

        if POST_URL:
            payload = {
                "id": POST_ID,
                "nome": str(porta),
                "url": url,
                "auth": AUTH_API
            }
            try:
                response = requests.post(POST_URL, json=payload)
                print("Status Code:", response.status_code)
                try:
                    print("Resposta:", response.json())
                except:
                    print("Resposta (raw):", response.text)
            except Exception as e:
                print("Erro ao enviar POST:", e)

    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
