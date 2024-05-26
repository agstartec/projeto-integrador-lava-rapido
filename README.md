  <h1>Sistema de Agendamentos para Lava-Jato</h1>
    <p>Este é um sistema de agendamentos desenvolvido em Flask para uma aplicação de lava-jato. O sistema permite que os usuários façam login, agendem serviços e visualizem os agendamentos.</p>

    <h2>Funcionalidades</h2>
    <ul>
        <li><strong>Login de Usuários:</strong> Permite que os usuários façam login no sistema.</li>
        <li><strong>Agendamento de Serviços:</strong> Permite que os usuários agendem serviços de lavagem de veículos.</li>
        <li><strong>Painel Administrativo:</strong> Permite que administradores visualizem todos os agendamentos.</li>
    </ul>

    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Python:</strong> Linguagem de programação principal.</li>
        <li><strong>Flask:</strong> Framework web utilizado para construir a aplicação.</li>
        <li><strong>SQLAlchemy:</strong> ORM utilizado para interagir com o banco de dados.</li>
        <li><strong>MySQL:</strong> Banco de dados utilizado para armazenar as informações.</li>
    </ul>

    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.6+</li>
        <li>Flask</li>
        <li>Flask-SQLAlchemy</li>
        <li>MySQL</li>
    </ul>

    <h2>Instalação</h2>
    <h3>1. Clonar o Repositório</h3>
    <pre><code>git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
    </code></pre>

    <h3>2. Criar um Ambiente Virtual</h3>
    <pre><code>python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
    </code></pre>

    <h3>3. Instalar as Dependências</h3>
    <pre><code>pip install -r requirements.txt
    </code></pre>

    <h3>4. Configurar o Banco de Dados</h3>
    <p>Crie um banco de dados MySQL e configure a URI de conexão no arquivo <code>app.py</code>:</p>
    <pre><code>app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<usuario>:<senha>@localhost/<nome_do_banco>'
    </code></pre>

    <h3>5. Inicializar o Banco de Dados</h3>
    <pre><code>from app import db
db.create_all()
    </code></pre>

    <h2>Uso</h2>
    <h3>Executar o Servidor</h3>
    <pre><code>python app.py
    </code></pre>
    <p>O servidor será iniciado em <code>http://127.0.0.1:5000</code>.</p>

    <h3>Rotas Disponíveis</h3>
    <ul>
        <li><code>GET /</code>: Página de login.</li>
        <li><code>POST /login</code>: Processa o login do usuário.</li>
        <li><code>POST /agendar</code>: Permite que um usuário agende um serviço.</li>
        <li><code>GET /painel</code>: Painel do usuário comum.</li>
        <li><code>GET /admin</code>: Painel do administrador.</li>
    </ul>

    <h2>Estrutura do Projeto</h2>
    <pre><code>seurepositorio/
<p>
│
├── app.py                  # Arquivo principal da aplicação</br>
├── requirements.txt        # Lista de dependências do projeto</br>
├── templates/              # Arquivos HTML</br>
├── login.html</br>
├── index.html</br>
├── admin.html</br>
└── assets/             # Arquivos estáticos (CSS, JS, imagens)</br>
│       └── ...</br>
└── README.md               # Este arquivo</br>
</p>
    </code></pre>

    <h2>Modelos de Dados</h2>
    <h3>Usuários</h3>
    <p>Tabela <code>usuarios</code>:</p>
    <ul>
        <li><strong>id:</strong> Identificador único (Integer, Primary Key)</li>
        <li><strong>user:</strong> Nome do usuário (String)</li>
        <li><strong>senha:</strong> Senha do usuário (String)</li>
        <li><strong>rule:</strong> Nível de permissão do usuário (Integer, 0 para usuário comum, 1 para administrador)</li>
    </ul>

    <h3>Agendamentos</h3>
    <p>Tabela <code>agendamentos</code>:</p>
    <ul>
        <li><strong>id:</strong> Identificador único (Integer, Primary Key)</li>
        <li><strong>veiculo:</strong> Modelo do veículo (String)</li>
        <li><strong>placa:</strong> Placa do veículo (String)</li>
        <li><strong>servico:</strong> Serviço solicitado (String)</li>
        <li><strong>endereco:</strong> Endereço do cliente (String)</li>
        <li><strong>nome:</strong> Nome do cliente (String)</li>
        <li><strong>telefone:</strong> Telefone do cliente (String)</li>
        <li><strong>data:</strong> Data do agendamento (Date)</li>
        <li><strong>hora:</strong> Hora do agendamento (String)</li>
    </ul>

    <h2>Contribuição</h2>
    <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.</p>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a MIT License.</p>