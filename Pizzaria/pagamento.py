class Pagamento:
    def __init__(self):
        #cardapio provisório
        self.metodo = [
            {"id": 1, "metodo": "Cartão de Crédito"},
            {"id": 2, "metodo": "Cartão de Débito"},
            {"id": 3, "metodo": "Dinheiro"},
            {"id": 4, "metodo": "Pix"},
            {"id": 5, "metodo": "Voucher"}
        ]
        self.itens = []

    def mostrar_metodo(self):
        print("Métodos de pagamento:")
        for item in self.metodo:
            print(f"ID: {item['id']} - Método: {item['metodo']}")
    
    def escolher_metodo(self, id_metodo):
        metodo = next((item for item in self.metodo if item["id"] == id_metodo), None)
        if metodo:
            print(f"Método de pagamento escolhido: {metodo['metodo']}")
            return metodo['metodo']
        else:
            print("Método inválido!")
            return None