#Codigo que vai mandar os dados do cliente para o banco de dados
import sqlite3

#Função para salvar os dados do usuario no banco de dados
def salvar_user(user):
    #Criação do banco de dados e da tabela de usuários
    con = sqlite3.connect('user.db')

    #Criar um objeto cursor para executar comandos SQL
    cur = con.cursor()

    #Criar a tabela de users
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL)''')

    #Verificar se o user já existe
    cur.execute("SELECT * FROM users WHERE email = ? AND senha = ?", (user.email, user.senha))
    if cur.fetchone():
        print("Usuário já existe!")
        pass
    else:
        cur.execute("INSERT INTO users (nome, email, senha)  VALUES (?,?,?)", (user.nome, user.email, user.senha))
        print("Usuário cadastrado com sucesso!")
        con.commit()

#Validar o Login do user
def validar_user(email, senha):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    
    cur.execute("SELECT * FROM users WHERE email = ? AND senha = ?", (email, senha))
    usuario = cur.fetchone()
    con.close()
    return usuario
    

def Relatorio(numero_pedido, user, sabores, quantidades, observacoes, precos, metodo):
    con = sqlite3.connect('Pedidos.db')
    cur = con.cursor()
    
    #Criar banco de dados
    cur.execute('''CREATE TABLE IF NOT EXISTS pedidos
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_pedido INTEGER NOT NULL,
                user TEXT NOT NULL,
                sabor TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                observacao TEXT,
                preco REAL NOT NULL,
                metodo TEXT NOT NULL)''')
                
    for i in range(len(sabores)):
        cur.execute('''INSERT INTO pedidos (numero_pedido, user, sabor, quantidade, observacao, preco, metodo)
                    VALUES (?,?,?,?,?,?,?)''', (numero_pedido, user, sabores[i], quantidades[i], observacoes[i], precos[i], metodo))
    con.commit()
    con.close()

