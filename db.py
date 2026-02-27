import sqlite3

def conectar():
    conn = sqlite3.connect('cadastro.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()

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
    conn.close()


def inserir_dados(nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios(nome, idade) VALUES (?, ?)", (nome, idade))
    print(f'Usuário {nome} adicionado a tabela usuários.')

    conn.commit()
    conn.close()