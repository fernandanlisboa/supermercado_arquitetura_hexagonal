from ..application.CaixaSupermercadoMain import CaixaSupermercado
from ..adapters.repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory
from ..adapters.RegistradoraAdapter import RegistradoraAdapter
from .ProdutoServiceTest import ProdutoServiceTest
from .VendaServiceTest import VendaServiceTest

class RegistradoraTest:

    def configurar_caixa(self):
        catalogo_de_produtos = CatalogoProdutosRepositoryMemory()
        catalogo_de_produtos.incluir_especificacao_produto(1, "Produto 1", 8.97)
        catalogo_de_produtos.incluir_especificacao_produto(2, "Produto 2", 0.0)
        registro = RegistradoraAdapter(catalogo_de_produtos)
        return registro
    
    def test_inicial(self):
        registro = self.configurar_caixa()
        registro.iniciar_venda()
        registro.incluir_item(1, 1)
        registro.incluir_item(2, 2)
        total = registro.get_total()
        print(total)
        assert total == 8.97
        print("Teste ok!")