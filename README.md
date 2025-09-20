# 🐳 Ngrok-Manage (Ngrok Tunnel Management with Docker)

This repository is a demo project for anyone who wants to learn about Docker and, most importantly, manage Ngrok tunnels efficiently. The application, built with Flask and Python, provides a web interface that allows you to create, monitor, and control Ngrok tunnels, all running inside a Docker container.

The main goal of this project is **Ngrok tunnel management**. Additionally, you will learn how to:

- Create a Dockerfile to package a Python application.
- Build and run a Docker container.
- Map ports and use volumes (-v) to persist Ngrok configuration data.

🛠️ Example Application

The application provides a simple web interface to:

- Start new Ngrok tunnels (HTTP/HTTPS).
- Monitor active tunnels and their public URLs.
- Stop or restart existing tunnels.

The interface makes it easy to manage tunnels without relying on the command line.

📁 Project Structure
```
Ngrok-Manage/
│
├── app.py                # Main Flask application logic
├── templates/
│   └── index.html        # HTML template for the homepage
├── static/
│   └── style.css         # Optional CSS for styling
├── ngrok_config.json     # Optional default configuration for Ngrok tunnels
├── requirements.txt      # Python dependencies (Flask)
└── Dockerfile            # Instructions to build the Docker image
```
🚀 How to Use and Learn

1. Build the Docker Image

Open your terminal in the project root and run:

docker build -t ngrok-manage:1.0 .

2. Prepare a Configuration Folder

Create a local folder to store Ngrok logs and configuration:

mkdir ~/ngrok_data

Place any Ngrok .json configuration files in this folder if needed.

3. Run the Container

Run the container, mounting the folder you created:

```
docker run -d \
  -p 5000:5000 \
  -v ~/ngrok_data:/root/ngrok_data \
  --name ngrok-manage \
  ngrok-manage:1.0
```
Explanation of parameters:

- `-d`: Runs the container in the background.
- `-p 5000:5000`: Maps port 5000 on your machine to port 5000 in the container.
- `-v ~/ngrok_data:/root/ngrok_data`: Connects the local folder to the container folder, persisting data.
- `--name ngrok-manage`: Assigns an easy-to-use name to the container.

4. Access the Application

Open your browser at:

http://localhost:5000

You will see the Ngrok tunnel management interface. Create, monitor, or stop tunnels. Changes to configuration files in the local folder are immediately reflected in the app.

🤝 Contributing

Feel free to use this project as a base for managing Ngrok tunnels and learning Docker/Flask. Suggestions or improvements can be submitted via issue or pull request.
