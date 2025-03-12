from ..core.ports.RegistradoraPort import RegistradoraPort
from .repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory
from ..core.ports.CatalogoProdutosPort import CatalogoProdutosPort
from ..core.services.ProdutoService import ProdutoService
from ..core.services.VendaService import VendaService

class RegistradoraAdapter(RegistradoraPort):
    """Implementação da porta de registro usando serviços para as regras de negócio"""
    
    def __init__(self, catalogo_de_produtos: CatalogoProdutosRepositoryMemory):
        self.servico_de_produto = ProdutoService(catalogo_de_produtos)
        self.servico_de_venda = VendaService(catalogo_de_produtos)
        self.catalogo_de_produtos = catalogo_de_produtos
    
    def incluir_especificacao_produto(self, id_: int, descricao: str, preco: float) -> None:
        try:
            self.servico_de_produto.adicionar_produto(id_, descricao, preco)
        except ValueError as e:
            print(f"Erro ao adicionar produto: {e}")
            # Reverter para a implementação básica sem validação
            # (para corresponder ao comportamento do código Java original)
            self.catalogo_de_produtos.incluir_especificacao_produto(id_, descricao, preco)
    
    def iniciar_venda(self) -> None:
        try:
            self.servico_de_venda.iniciar_nova_venda()
        except Exception as e:
            print(f"Erro ao iniciar venda: {e}")
    
    def incluir_item(self, id_produto: int, quantidade: int) -> None:
        try:
            self.servico_de_venda.adicionar_item_na_venda(id_produto, quantidade)
        except ValueError as e:
            print(f"Erro ao adicionar item: {e}")
    
    def get_total(self) -> float:
        try:
            return self.servico_de_venda.obter_total_da_venda_atual()
        except ValueError:
            return 0.0
    
    def get_troco(self, valor_pago: float) -> float:
        try:
            return self.servico_de_venda.concluir_venda(valor_pago)
        except ValueError as e:
            print(f"Erro ao concluir venda: {e}")
            return 0.0
    
    def get_catalogo_produtos(self):
        return self.catalogo_de_produtos
