from flask import Flask, render_template, request, jsonify
import os

# Descobre o caminho absoluto da pasta onde este arquivo (index.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Aponta para as pastas templates e static subindo um nível usando caminhos absolutos
app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, '../templates'),
            static_folder=os.path.join(BASE_DIR, '../static'))

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