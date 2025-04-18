#codigo para cadastro de usuario numa pizzaria
#criação do objeto user com os atributos nome, email e senha
class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#coleta de informações do usuario
    def cadastro_cliente():
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        return User(nome, email, senha)
    

