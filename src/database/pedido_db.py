import sqlite3

def Relatorio(numero_pedido, user, sabores, quantidades, observacoes, precos, metodo):
    con = sqlite3.connect('Pedidos.db')
    cur = con.cursor()
    
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