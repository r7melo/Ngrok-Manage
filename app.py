from flask import Flask, jsonify, render_template, request
import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ----------------------------
# Comandos globais
# ----------------------------
SSH_KILL_NGROK = "pkill ngrok"

SSH_TCP_COMMAND = """
nohup ngrok tcp 22 --log=stdout > ngrok_tcp.log 2>&1 &
sleep 2
grep -o 'tcp://[0-9a-zA-Z:.]*' ngrok_tcp.log | head -n1
"""

def ssh_http_command(port: str) -> str:
    return f"""
nohup ngrok http {port} --log=stdout > ngrok_http.log 2>&1 &
sleep 2
grep -o 'https://[0-9a-zA-Z:.]*' ngrok_http.log | head -n1
"""

# ----------------------------
# Função global para executar comandos via SSH
# ----------------------------
def run_ssh_command(command: str) -> str:
    host = os.getenv("SSH_HOST")
    username = os.getenv("SSH_USER")
    password = os.getenv("SSH_PASS")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=22, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        ssh.close()

        if error and not output:
            return f"Erro: {error}"
        return output if output else "Comando executado, mas sem saída."

    except Exception as e:
        return str(e)

# ----------------------------
# Rotas
# ----------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ssh_kill_ngrok", methods=["POST"])
def ssh_kill_ngrok():
    return jsonify({"output": run_ssh_command(SSH_KILL_NGROK)})


@app.route("/ssh_exec_tcp", methods=["POST"])
def ssh_exec_tcp():
    # Primeiro mata qualquer ngrok ativo
    run_ssh_command(SSH_KILL_NGROK)
    return jsonify({"output": run_ssh_command(SSH_TCP_COMMAND)})


@app.route("/ssh_exec_http", methods=["POST"])
def ssh_exec_http():
    data = request.get_json()
    port = data.get("port", "80")
    # Primeiro mata qualquer ngrok ativo
    run_ssh_command(SSH_KILL_NGROK)
    return jsonify({"output": run_ssh_command(ssh_http_command(port))})


# ----------------------------
# Inicializa o app
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
