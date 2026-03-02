import sqlite3

def conectar():
    conn = sqlite3.connect('cadastro.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY, 
                nome TEXT,
                idade INTEGER
            )
            """
            )
        print('tabela usuários criada!')
        
        conn.commit()
    finally:
        conn.close()


def inserir_dados(nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO usuarios(nome, idade) VALUES (?, ?)", (nome, idade))
        print(f'Usuário {nome} adicionado a tabela usuários.')

        conn.commit()
    finally:
        conn.close()



def listar_dados():
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()

        for dado in dados:
            print(f"ID:{dado['id']} - Nome:{dado['nome']} - Idade:{dado['idade']}")
    finally:
        conn.close()


def listar_dados_ID(usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id, ))
        dado = cursor.fetchone()

        if dado:
            print(f"Nome: {dado['nome']} - Idade: {dado['idade']}")
        else:
            print("Usuário não encontrado")
    finally:
        conn.close()