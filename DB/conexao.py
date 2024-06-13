import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def remover_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_registros_lote(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()

def buscar_registros(cursor):
    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

def buscar_registro_unico(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    print(resultado)

#inserir_registro(conexao, cursor, "César", "cesar@gmail.com")
#remover_registro(conexao, cursor, 1)
dados = [
    ("Maria", "maria@gmail"),
    ("Celso", "celso@gmail"),
    ("rafael", "rafael@gmail"),
    ("Lucia", "Lucia@gmail")
]
#inserir_registros_lote(conexao, cursor, dados)
#buscar_registros(conexao, cursor)
buscar_registro_unico(conexao, cursor, 2)


