from ..ports.CatalogoProdutosPort import CatalogoProdutosPort
from ..entity.EspecificacaoProdutoEntity import EspecificacaoProdutoEntity

class ProdutoService:
    """Serviço para as regras de negócio relacionadas aos produtos"""
    
    def __init__(self, catalogo_de_produtos: CatalogoProdutosPort):
        self.catalogo_de_produtos = catalogo_de_produtos
    
    def adicionar_produto(self, id_: int, descricao: str, preco: float) -> EspecificacaoProdutoEntity:
        """
        Adicionar um produto ao catálogo com validação das regras de negócio
        - O preço deve ser positivo
        - A descrição não pode ser vazia
        - O ID deve ser positivo
        """
        print(id, preco, descricao)
        if preco < 0:
            raise ValueError("O preço do produto deve ser positivo")

        if not descricao or not descricao.strip():
            raise ValueError("A descrição do produto não pode ser vazia")

        if id_ <= 0:
            raise ValueError("O ID do produto deve ser positivo")

        self.catalogo_de_produtos.incluir_especificacao_produto(id_, descricao, preco)
        return self.catalogo_de_produtos.obter_especificacao_produto(id_)
    
    def obter_produto(self, id_: int) -> EspecificacaoProdutoEntity:
        """Obter um produto pelo ID com validação"""
        if id_ <= 0:
            raise ValueError("O ID do produto deve ser positivo")
            
        produto = self.catalogo_de_produtos.obter_especificacao_produto(id_)
        if produto is None:
            raise ValueError(f"Produto com ID {id_} não encontrado")
            
        return produto
