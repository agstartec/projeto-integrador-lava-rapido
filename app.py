from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/lava_jato'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)
# Definindo um modelo de exemplo
class Usuarios(db.Model):
    __tablename__= "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    rule = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, id, user, senha, rule):
        return f'Usuario(id={self.id}, nome={self.user}, email={self.senha})'

# Lista para armazenar os agendamentos
with app.app_context():
    # Lista para armazenar os agendamentos
    usuarios = Usuarios.query.all()
    for usuario in usuarios:
        print(f'ID: {usuario.id}, Nome: {usuario.user}, Email: {usuario.senha}')
agendamentos = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/assets/<path:filename>')
def serve_css(filename):
    return send_from_directory('templates/assets', filename)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':       
        usuario = request.form['usuario']
        senha = request.form['senha']
        print(usuario)
        print(senha)
        if usuario and senha:
            user = Usuarios.query.filter_by(user=usuario).first()
            if user and user.senha == senha:
                if user.rule == 0:
                    return redirect('painel')
                elif user.rule == 1:
                    return redirect('admin')
                else:
                    return render_template('login.html')
        else:
            return render_template('login.html')

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

@app.route('/painel')
def painel():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
