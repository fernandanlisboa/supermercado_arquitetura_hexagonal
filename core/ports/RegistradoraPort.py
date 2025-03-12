from abc import ABC, abstractmethod

class RegistradoraPort(ABC):
    """Porta para operações da registradora"""
    
    @abstractmethod
    def incluir_especificacao_produto(self, id_: int, descricao: str, preco: float) -> None:
        """Inclui uma especificação de produto no catálogo"""
        pass
    
    @abstractmethod
    def iniciar_venda(self) -> None:
        """Inicia uma nova venda"""
        pass
    
    @abstractmethod
    def incluir_item(self, id_produto: int, quantidade: int) -> None:
        """Inclui um item na venda atual"""
        pass
    
    @abstractmethod
    def get_total(self) -> float:
        """Obtém o valor total da venda atual"""
        pass
    
    @abstractmethod
    def get_troco(self, valor_pago: float) -> float:
        """Obtém o troco para a venda atual"""
        pass
    
    @abstractmethod
    def get_catalogo_produtos(self):
        """Obtém o catálogo de produtos"""
        pass
