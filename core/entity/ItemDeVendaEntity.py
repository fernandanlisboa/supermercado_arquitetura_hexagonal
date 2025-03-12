class ItemDeVendaEntity:
    """Modelo de domínio para um item em uma venda"""
    
    def __init__(self, especificacao_produto, quantidade: int):
        self.quantidade = quantidade
        self.especificacao_produto = especificacao_produto
    
    def get_subtotal(self):
        subtotal = self.quantidade * self.especificacao_produto.get_preco()
        print(f"SubTotal: {subtotal}")
        import time
        time.sleep(1)  
        return subtotal
