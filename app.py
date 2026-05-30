from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.datetime.now()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Final Project</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
                margin-top: 50px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }}
            .container {{
                background: rgba(255,255,255,0.1);
                border-radius: 20px;
                padding: 40px;
                margin: 20px auto;
                width: 80%;
                max-width: 700px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }}
            h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
            .status {{
                color: #4ade80;
                font-weight: bold;
                font-size: 1.2em;
            }}
            .tech {{
                display: inline-block;
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                margin: 10px;
                border-radius: 10px;
                font-family: monospace;
            }}
            .time {{
                font-size: 0.9em;
                margin-top: 30px;
                opacity: 0.8;
            }}
            button {{
                background: #4ade80;
                color: #333;
                border: none;
                padding: 10px 30px;
                border-radius: 5px;
                font-size: 1em;
                cursor: pointer;
                margin-top: 20px;
            }}
            button:hover {{
                background: #22c55e;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 DevOps Final Project</h1>
            <h2>Sistemas Operativos II</h2>
            <hr>
            <p>✅ Infraestructura desplegada exitosamente en <span class="status">AWS EC2</span></p>
            <p>🔄 Pipeline CI/CD funcionando con <span class="status">GitHub Actions</span></p>
            <p>🐳 Contenedores orquestados con <span class="status">Docker Compose</span></p>
            <p>🔐 Conexión segura mediante <span class="status">SSH Keys</span></p>
            
            <div>
                <span class="tech">🐍 Python Flask</span>
                <span class="tech">🐳 Docker</span>
                <span class="tech">☁️ AWS EC2</span>
                <span class="tech">🔄 GitHub Actions</span>
            </div>
            
            <button onclick="location.reload()">🔄 Actualizar</button>
            
            <div class="time">
                📅 Despliegue automático activado<br>
                Última actualización: {now.strftime('%Y-%m-%d %H:%M:%S')}
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK", 200

@app.route('/status')
def status():
    return {
        "status": "running",
        "service": "devops-final-project",
        "version": "1.0.0"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
