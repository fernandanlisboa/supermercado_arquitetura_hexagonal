from abc import ABC, abstractmethod
from ..model.EspecificacaoProduto import EspecificacaoProduto

class PortaVenda(ABC):
    """Porta para operações de venda"""
    
    @abstractmethod
    def incluir_item(self, EspecificacaoProduto: EspecificacaoProduto, quantidade: int) -> None:
        """Inclui um item na venda"""
        pass
    
    @abstractmethod
    def get_total(self) -> float:
        """Obtém o valor total da venda"""
        pass
    
    @abstractmethod
    def get_troco(self, valor_pago: float) -> float:
        """Obtém o troco da venda"""
        pass
