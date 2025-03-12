class EspecificacaoProdutoEntity:
    def __init__(self, id_: int, descricao: str, preco: float):
        self.id = id_
        self.descricao = descricao
        self.preco = preco
    
    def get_descricao(self):
        return self.descricao
    
    def get_preco(self):
        print(f"Preço: {self.preco}")
        import time
        time.sleep(1) 
        return self.preco
    
    def __str__(self):
        return f"{self.id} {self.descricao} {self.preco}"
