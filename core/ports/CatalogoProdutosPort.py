from abc import ABC, abstractmethod
from ..entity.EspecificacaoProdutoEntity import EspecificacaoProdutoEntity

class CatalogoProdutosPort(ABC):
    """Porta para operações do catálogo de produtos"""
    
    @abstractmethod
    def obter_especificacao_produto(self, id_: int) -> EspecificacaoProdutoEntity:
        """Obtém a especificação de um produto pelo ID"""
        pass
    
    @abstractmethod
    def incluir_especificacao_produto(self, id_: int, descricao: str, preco: float) -> None:
        """Inclui uma especificação de produto no catálogo"""
        pass
