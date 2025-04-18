#Codigo principal do sistema de pedidos

from Login_user import User
from armazenamento import salvar_user, validar_user, Relatorio
from Pedido_user import Pedido
from pagamento import Pagamento
import random

print("----------------------")
print("|   1 - Cadastro     |")
print("|   2 - Login        |")
print("|   3 - Sair         |")
print("----------------------")


match input("Escolha uma opção: "):
    #Cadastrar um novo User
    case "1":
        user1 = User.cadastro_cliente()
        salvar_user(user1)
        print("Bem-vindo(a) ao sistema!\n", user1.nome)

        pedido = Pedido()
        pedido.mostrar_cardapio()

        continuar = "s"
        while continuar.lower() == "s":
            try:
                id_sabor = int(input("Digite o ID do sabor desejado: "))
                quantidade = float(input("Digite a quantidade desejada: "))
                observacao = input("Digite uma observação (se não, deixe em branco): ")
                pedido.adicionar_pizza(id_sabor, quantidade, observacao)
    
            except ValueError:
                print("Entrada inválida! Tente novamente.")
            continuar = input("Deseja adicionar mais pizzas? (s/n): ")

        pedido.mostrar_pedido()
        pagamento = Pagamento()
        pagamento.mostrar_metodo()
        id_metodo = int(input("Escolha o método de pagamento (1-5): "))
    
        metodo_escolhido = pagamento.escolher_metodo(id_metodo)
        if metodo_escolhido:
         pass
        else:
            print("Método inválido!")

        numero_pedido = random.randint(1000, 9999)
        user = user1.nome


        sabores = []
        quantidades = []
        observacoes = []
        precos = []
        total_pedido = 0

        for item in pedido.itens:
            sabores.append(item["sabor"])
            quantidades.append(item["quantidade"])
            observacoes.append(item["observacao"])
            precos.append(item["preco_total"])
            total_pedido += item["preco_total"]  # Somando o preço total
            
        Relatorio(numero_pedido, user, sabores, quantidades, observacoes, precos, metodo_escolhido)
        print(f"Seu número de pedido é: {numero_pedido}")
        print(f"Total: R$ {pedido.calcular_total():.2f}")
        print("Obrigado por usar nosso sistema!")

    #Fazer login
    case "2":
        
        email_user = input("Digite seu email: ")
        senha_user = input("Digite sua senha: ")

        if validar_user(email_user, senha_user):
            
            print("Login realizado com sucesso!\n")
            usuario_logado = validar_user(email_user, senha_user)

            pedido = Pedido()
            pedido.mostrar_cardapio()

            continuar = "s"
            while continuar.lower() == "s":
                try:
                    id_sabor = int(input("Digite o ID do sabor desejado: "))
                    quantidade = float(input("Digite a quantidade desejada: "))
                    observacao = input("Digite uma observação (se não, deixe em branco): ")
                    pedido.adicionar_pizza(id_sabor, quantidade, observacao)
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                continuar = input("Deseja adicionar mais pizzas? (s/n): ")


            pedido.mostrar_pedido()
            pagamento = Pagamento()
            pagamento.mostrar_metodo()
            id_metodo = int(input("Escolha o método de pagamento (1-5): "))
    
            metodo_escolhido = pagamento.escolher_metodo(id_metodo)
            if metodo_escolhido:
             pass
            else:
             print("Método inválido!")
        else:
            print("Email ou senha inválidos!")


        numero_pedido = random.randint(1000, 9999)
        user = usuario_logado[2]
        sabores = []
        quantidades = []
        observacoes = []
        precos = []
        total_pedido = 0

        for item in pedido.itens:
            sabores.append(item["sabor"])
            quantidades.append(item["quantidade"])
            observacoes.append(item["observacao"])
            precos.append(item["preco_total"])
            total_pedido += item["preco_total"]  # Somando o preço total
            
        Relatorio(numero_pedido, user, sabores, quantidades, observacoes, precos, metodo_escolhido)
        print(f"Seu número de pedido é: {numero_pedido}")
        print(f"Total: R$ {pedido.calcular_total():.2f}")
        print("Obrigado por usar nosso sistema!")
        
        #Sair do sistema
    case "3":
        print("Saindo do sistema...")
        exit()

    #Se o User colocar algo fora do esperado
    case default:
        print("Opção inválida! Por isso estou saindo...")
        print("Saindo do sistema...")
        exit()
