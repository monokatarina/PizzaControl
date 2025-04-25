from services.auth_service import cadastrar_usuario, fazer_login
from services.pedido_service import processar_pedido

def mostrar_menu():
    print("----------------------")
    print("|   1 - Cadastro     |")
    print("|   2 - Login        |")
    print("|   3 - Sair         |")
    print("----------------------")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                usuario = cadastrar_usuario()
                if usuario:
                    processar_pedido(usuario)
            case "2":
                usuario = fazer_login()
                if usuario:
                    processar_pedido(usuario)
            case "3":
                print("Saindo do sistema...")
                exit()
            case _:
                print("Opção inválida! Por isso estou saindo...")
                print("Saindo do sistema...")
                exit()

if __name__ == "__main__":
    main()