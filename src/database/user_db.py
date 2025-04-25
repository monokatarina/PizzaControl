import sqlite3

def salvar_user(user):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL)''')

    cur.execute("SELECT * FROM users WHERE email = ? AND senha = ?", (user.email, user.senha))
    if cur.fetchone():
        print("Usuário já existe!")
        pass
    else:
        cur.execute("INSERT INTO users (nome, email, senha) VALUES (?,?,?)", (user.nome, user.email, user.senha))
        print("Usuário cadastrado com sucesso!")
        con.commit()

def validar_user(email, senha):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    
    cur.execute("SELECT * FROM users WHERE email = ? AND senha = ?", (email, senha))
    usuario = cur.fetchone()
    con.close()
    return usuario