from ...core.ports.CatalogoProdutosPort import CatalogoProdutosPort
from ...core.entity.EspecificacaoProdutoEntity import EspecificacaoProdutoEntity

class CatalogoProdutosRepositoryMemory(CatalogoProdutosPort):
    """Implementação em memória da porta de catálogo de produtos"""
    
    def __init__(self):
        self.mapa_de_especificacoes = {}
    
    def obter_especificacao_produto(self, id_: int) -> EspecificacaoProdutoEntity:
        return self.mapa_de_especificacoes.get(id_)
    
    def incluir_especificacao_produto(self, id_: int, descricao: str, preco: float) -> None:
        especificacao_produto = EspecificacaoProdutoEntity(id_, descricao, preco)
        self.mapa_de_especificacoes[id_] = especificacao_produto
