import random
from models.pedido import Pedido
from models.pagamento import Pagamento
from database.pedido_db import Relatorio

def processar_pedido(usuario):
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
    if not metodo_escolhido:
        print("Método inválido!")
        return

    numero_pedido = random.randint(1000, 9999)
    user = usuario.nome if hasattr(usuario, 'nome') else usuario[2]

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
        total_pedido += item["preco_total"]

    Relatorio(numero_pedido, user, sabores, quantidades, observacoes, precos, metodo_escolhido)
    
    print(f"Seu número de pedido é: {numero_pedido}")
    print(f"Total: R$ {pedido.calcular_total():.2f}")
    print("Obrigado por usar nosso sistema!")