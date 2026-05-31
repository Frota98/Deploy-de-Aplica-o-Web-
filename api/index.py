from flask import Flask, render_template, request, jsonify
import os

# Mapeamento estrito do diretório
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, '../templates'),
            static_folder=os.path.join(BASE_DIR, '../static'))

# Rota principal (Renderiza o HTML)
@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        # Se o Flask não achar a pasta templates por erro de estrutura, 
        # ele exibe este HTML de emergência para a página não quebrar.
        return f"<h1>Aplicação Python no Ar!</h1><p>Erro ao carregar template: {str(e)}</p>"

# Rota de API (Integração Front e Back)
@app.route('/api/feedback', methods=['POST'])
def feedback():
    try:
        dados = request.get_json() or {}
        nome = dados.get('nome', 'Visitante')
        mensagem = dados.get('mensagem', '')
        
        resposta_texto = f"Olá, {nome}! Seu feedback ('{mensagem}') foi processado com sucesso pelo servidor Python."
        
        return jsonify({
            "status": "sucesso",
            "mensagem_servidor": respuesta_texto
        })
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

# Garante que a Vercel encontre o objeto WSGI da aplicação
app.debug = False