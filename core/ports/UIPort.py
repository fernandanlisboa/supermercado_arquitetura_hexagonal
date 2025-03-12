from abc import ABC, abstractmethod

class UIPort(ABC):
    """Porta para operações da interface do usuário"""
    
    @abstractmethod
    def run(self) -> None:
        """Executar a interface do usuário"""
        pass