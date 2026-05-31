from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
            static_folder=os.path.join(os.path.dirname(__file__), '../static'))

# Rota principal para carregar a página
@app.route('/')
def home():
    return render_template('index.html')

# Rota de API para receber dados do Front-end (Integração)
@app.route('/api/feedback', methods=['POST'])
def feedback():
    dados = request.get_json()
    nome = dados.get('nome', 'Visitante')
    mensagem = dados.get('mensagem', '')
    
    # Processamento simples no Back-end
    resposta_texto = f"Olá, {nome}! Seu feedback ('{mensagem}') foi processado com sucesso pelo servidor Python."
    
    return jsonify({
        "status": "sucesso",
        "mensagem_servidor": respuesta_texto
    })

# Necessário para a Vercel expor o app corretamente
def handler(request, client):
    return app(request, client)