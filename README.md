# 📝 **PizzaControl** - Sistema de Gerenciamento de Pizzaria 🍕

---

## 📌 **Descrição**
Sistema completo para gerenciamento de pedidos em uma pizzaria, incluindo:
- Cadastro e autenticação de usuários
- Cardápio interativo
- Gestão de pedidos
- Processamento de pagamentos
- Geração de relatórios

---

## 🛠 **Tecnologias Utilizadas**
- **Python** (Linguagem principal)
- **SQLite** (Banco de dados)
- **POO** (Programação Orientada a Objetos)
- **Modularização** (Organização de código)

---

## 📂 **Estrutura do Projeto**

```
PizzaControl/
├── src/
│   ├── models/               # Modelos de dados
│   │   ├── user.py           # Classe Usuário
│   │   ├── pedido.py         # Classe Pedido
│   │   └── pagamento.py      # Classe Pagamento
│   │
│   ├── database/             # Operações com banco de dados
│   │   ├── user_db.py        # CRUD de usuários
│   │   └── pedido_db.py      # Registro de pedidos
│   │
│   ├── services/             # Lógica de negócios
│   │   ├── auth_service.py   # Autenticação
│   │   └── pedido_service.py # Processamento de pedidos
│   │
│   └── main.py               # Ponto de entrada
├── README.md                 # Este arquivo
└── requirements.txt          # Dependências
```

---

## 🚀 **Como Executar**

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/PizzaControl.git
   cd PizzaControl
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema**
   ```bash
   python src/main.py
   ```

---

## 🎨 **Interface do Sistema**

### **Menu Principal**
```
----------------------
|   1 - Cadastro     |
|   2 - Login        |
|   3 - Sair         |
----------------------
```

### **Fluxo do Usuário**
1. Cadastre-se ou faça login
2. Visualize o cardápio
3. Adicione pizzas ao pedido
4. Escolha método de pagamento
5. Confirme o pedido

---

## 💡 **Funcionalidades Principais**

✔ **Cadastro de Usuários**  
✔ **Autenticação Segura**  
✔ **Cardápio Dinâmico**  
✔ **Pedidos Personalizados** (com observações)  
✔ **Múltiplas Formas de Pagamento**  
✔ **Relatórios Automatizados**  
✔ **Persistência em Banco de Dados**  

---

## 📊 **Banco de Dados**

- **user.db**: Armazena dados dos usuários
  ```sql
  CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      senha TEXT NOT NULL
  )
  ```

- **Pedidos.db**: Registra histórico de pedidos
  ```sql
  CREATE TABLE pedidos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      numero_pedido INTEGER NOT NULL,
      user TEXT NOT NULL,
      sabor TEXT NOT NULL,
      quantidade INTEGER NOT NULL,
      observacao TEXT,
      preco REAL NOT NULL,
      metodo TEXT NOT NULL
  )
  ```

---
