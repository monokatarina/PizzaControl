from database.user_db import salvar_user, validar_user
from models.user import User

def cadastrar_usuario():
    user = User.cadastro_cliente()
    salvar_user(user)
    print("Bem-vindo(a) ao sistema!\n", user.nome)
    return user

def fazer_login():
    email_user = input("Digite seu email: ")
    senha_user = input("Digite sua senha: ")

    usuario = validar_user(email_user, senha_user)
    if usuario:
        print("Login realizado com sucesso!\n")
        return usuario
    else:
        print("Email ou senha inválidos!")
        return None