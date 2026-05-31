from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

# Rota principal para carregar a página
@app.route('/')
def home():
    return render_template('index.html')

# Rota de API para receber dados do Front-end (Integração)
@app.route('/api/feedback', methods=['POST'])
def feedback():
    try:
        dados = request.get_json()
        nome = dados.get('nome', 'Visitante')
        mensagem = dados.get('mensagem', '')
        
        resposta_texto = f"Olá, {nome}! Seu feedback ('{mensagem}') foi processado com sucesso pelo servidor Python."
        
        return jsonify({
            "status": "sucesso",
            "mensagem_servidor": respuesta_texto
        })
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500