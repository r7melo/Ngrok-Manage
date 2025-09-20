// ----------------------------
// Bloqueio geral apenas dos .action-host
// ----------------------------
function disableAll() {
    document.querySelectorAll(".action-host").forEach(btn => {
        btn.disabled = true;
        btn.textContent = "Executando...";
    });

    document.querySelectorAll(".output-host").forEach(pre => {
        pre.textContent = ' '
    });
}

function enableAll() {
    document.querySelectorAll(".action-host").forEach(btn => {
        btn.disabled = false;
        btn.textContent = btn.getAttribute("data-original") || "Executar";
    });
}

// ----------------------------
// Envio de comandos
// ----------------------------
async function sendCommand(route, inputId, outputId, button) {
    let bodyData = {};
    if (inputId) {
        const value = document.getElementById(inputId).value;
        bodyData.port = value;
    }

    // Salva texto original só uma vez
    if (!button.getAttribute("data-original")) {
        button.setAttribute("data-original", button.textContent);
    }

    disableAll();

    try {
        const response = await fetch(route, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: Object.keys(bodyData).length ? JSON.stringify(bodyData) : null
        });
        const data = await response.json();
        document.getElementById(outputId).textContent = formatNgrokOutput(data.output);
    } catch (err) {
        document.getElementById(outputId).textContent = "Erro: " + err;
    }

    enableAll();
}

// ----------------------------
// Funções específicas
// ----------------------------
function startTcp(btn) {
    sendCommand("/ssh_exec_tcp", null, "tcpOutput", btn);
}

function startHttp(btn) {
    sendCommand("/ssh_exec_http", "httpPortInput", "httpOutput", btn);
}

function formatNgrokOutput(ngrokUrl) {
  try {
    if (ngrokUrl.startsWith('tcp://')) {
      const url = new URL(ngrokUrl);
      const hostname = url.hostname;
      const port = url.port;
      const customId = 'hm0b';
      return `ssh ${customId}@${hostname} -p ${port}`;
    } else {
      return ngrokUrl.replace('ngrok', 'ngrok-free.app');
    }
  } catch (e) {
    return 'URL inválida';
  }
}
