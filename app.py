from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime

app = Flask(__name__)

# Lista para armazenar os agendamentos
agendamentos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets/<path:filename>')
def serve_css(filename):
    return send_from_directory('templates/assets', filename)

@app.route('/agendar', methods=['POST'])
def agendar():
    if request.method == 'POST':
        veiculo = request.form['veiculo']
        placa = request.form['placa']
        servico = request.form['servico']
        endereco = request.form['endereco']
        nome = request.form['nome']
        telefone = request.form['telefone']
        data_hora = request.form['data_hora']
        
        agendamentos.append({
            'veiculo': veiculo,
            'placa': placa,
            'servico': servico,
            'endereco': endereco,
            'nome': nome,
            'telefone': telefone,
            'data_hora': data_hora
        })
        return redirect(url_for('index'))

@app.route('/admin')
def admin():
    return render_template('admin.html', agendamentos=agendamentos)

if __name__ == '__main__':
    app.run(debug=True)
