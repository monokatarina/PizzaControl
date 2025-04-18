#Criação do objeto pedido
class Pedido:
    def __init__(self):
        #cardapio provisório
        self.pedido = [
            {"id": 1, "sabor": "Calabresa", "preco": 30.0},
            {"id": 2, "sabor": "Frango com Catupiry", "preco": 35.0},
            {"id": 3, "sabor": "Margherita", "preco": 28.0 },
            {"id": 4, "sabor": "Quatro Queijos", "preco": 32.0},
            {"id": 5, "sabor": "Portuguesa", "preco": 33.0},
            {"id": 6, "sabor": "Napolitana", "preco": 31.0},
            {"id": 7, "sabor": "Toscana", "preco": 34.0}
        ]
        self.itens = []


    def mostrar_cardapio(self):
        print("Cardápio:")
        for item in self.pedido:
            print(f"ID: {item['id']} - Sabor: {item['sabor']} - Preço: R$ {item['preco']:.2f}")
    
    #Função que vai adcionar a pizza ao pedido
    def adicionar_pizza(self, id_sabor, quantidade, observacao=""):
        sabor = next((item for item in self.pedido if item["id"] == id_sabor), None)
        if sabor:
            item = {
                "sabor": sabor["sabor"],
                "quantidade": quantidade,
                "observacao": observacao,
                "preco_unitario": sabor["preco"],
                "preco_total": sabor["preco"] * quantidade
            }
            self.itens.append(item)
            print(f"Pizza {sabor['sabor']} adicionada ao pedido!")
        else:
            print("Sabor inválido!")
    #Mostrar o pedido para o user
    def mostrar_pedido(self):
        print("Pedido:")
        for item in self.itens:
                print(f"{item['quantidade']}x {item['sabor']} - R$ {item['preco_unitario'] * item['quantidade']:.2f}")
                print(f"Observação: {item['observacao']}")
        print(f"Total: R$ {self.calcular_total():.2f}")
        
    #Calcular o total do pedido
    def calcular_total(self):
        total = sum(item["preco_total"] for item in self.itens)
        return total