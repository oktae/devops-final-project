from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Final Project</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .card {{
                background: rgba(255,255,255,0.95);
                border-radius: 20px;
                padding: 40px;
                width: 90%;
                max-width: 600px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                text-align: center;
            }}
            h1 {{ color: #667eea; margin-bottom: 10px; }}
            h2 {{ color: #764ba2; margin-bottom: 20px; }}
            .badge {{
                display: inline-block;
                background: #4ade80;
                color: #fff;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 14px;
                margin: 10px 0;
            }}
            .tech {{
                display: inline-block;
                background: #f3f4f6;
                padding: 8px 16px;
                margin: 5px;
                border-radius: 8px;
                font-family: monospace;
                font-size: 14px;
            }}
            .status {{
                color: #22c55e;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #6b7280;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎓 DevOps Final Project</h1>
            <h2>Sistemas Operativos II</h2>
            <div class="badge">👤 Estudiante: oktae</div>
            
            <hr style="margin: 20px 0;">
            
            <p>✅ <span class="status">Infraestructura Cloud</span> - AWS EC2</p>
            <p>🔄 <span class="status">CI/CD Pipeline</span> - GitHub Actions</p>
            <p>🐳 <span class="status">Contenedores</span> - Docker Compose</p>
            <p>🔐 <span class="status">Seguridad</span> - SSH Keys</p>
            
            <div style="margin: 20px 0;">
                <span class="tech">🐍 Python Flask</span>
                <span class="tech">🐳 Docker</span>
                <span class="tech">☁️ AWS</span>
                <span class="tech">🔄 GitHub Actions</span>
            </div>
            
            <div class="footer">
                📅 Último despliegue: {now.strftime('%Y-%m-%d %H:%M:%S')}<br>
                🔄 Despliegue automático activado
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "service": "up"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
