from ..ports.CatalogoProdutosPort import CatalogoProdutosPort
from ..entity.VendaEntity import VendaEntity

class VendaService:
    """Serviço para as regras de negócio relacionadas à venda"""
    
    def __init__(self, catalogo_de_produtos: CatalogoProdutosPort):
        self.catalogo_de_produtos = catalogo_de_produtos
        self.venda_atual = None
    
    def iniciar_nova_venda(self) -> VendaEntity:
        """Iniciar uma nova venda com validação"""
        # Regra de negócio: Não é possível iniciar uma nova venda se uma já estiver em andamento
        if self.venda_atual is not None:
            # Decisão de negócio: Vamos concluir a venda atual e iniciar uma nova
            self.venda_atual = VendaEntity()
        else:
            self.venda_atual = VendaEntity()
            
        return self.venda_atual
    
    def adicionar_item_na_venda(self, id_produto: int, quantidade: int) -> bool:
        """
        Adicionar um item à venda atual com as regras de negócio
        - A quantidade deve ser positiva
        - O produto deve existir
        - A venda deve estar em andamento
        """
        if self.venda_atual is None:
            raise ValueError("Nenhuma venda em andamento. Comece uma nova venda primeiro.")
            
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser positiva")
            
        especificacao_produto = self.catalogo_de_produtos.obter_especificacao_produto(id_produto)
        if especificacao_produto is None:
            # Regra de negócio: Pular produtos inválidos ao invés de falhar
            print(f"Produto com ID {id_produto} não encontrado, pulando")
            return False
            
        self.venda_atual.incluir_item(especificacao_produto, quantidade)
        return True
    
    def concluir_venda(self, valor_pago: float) -> float:
        """
        Concluir a venda atual e calcular o troco
        - O valor pago deve ser suficiente
        - A venda deve estar em andamento
        """
        if self.venda_atual is None:
            raise ValueError("Nenhuma venda em andamento. Comece uma nova venda primeiro.")
            
        total = self.venda_atual.get_total()
        print(f"total: {total}")
        
        # Regra de negócio: O valor pago deve cobrir o total
        if valor_pago < total:
            raise ValueError(f"Pagamento insuficiente. O total é {total}, pago {valor_pago}")
            
        troco = self.venda_atual.get_troco(valor_pago)
        
        # Não resetamos a venda_atual aqui para que o recibo ainda possa ser impresso
        # Em uma aplicação real, você pode querer armazenar a venda em um repositório
        
        return troco
    
    def obter_total_da_venda_atual(self) -> float:
        """Obter o total da venda atual com validação"""
        if self.venda_atual is None:
            raise ValueError("Nenhuma venda em andamento. Comece uma nova venda primeiro.")
            
        return self.venda_atual.get_total()
        
    def obter_venda_atual(self) -> VendaEntity:
        """Obter a venda atual"""
        return self.venda_atual
