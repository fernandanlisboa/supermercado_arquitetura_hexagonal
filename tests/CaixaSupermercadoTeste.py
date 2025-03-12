from .CatalogoProdutosTest import CatalogoProdutosTest
from ..adapters.repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory
from .RegistradoraTest import RegistradoraTest
from ..adapters.ui.UIConsoleAdapter import UIConsoleAdapter

class CaixaSupermercadoTeste:
    """Classe principal da aplicação"""
    
    def __init__(self, usar_catalogo_em_arquivo=False, caminho_arquivo=None):
        if usar_catalogo_em_arquivo and caminho_arquivo:
            self.catalogo_de_produtos = CatalogoProdutosTest(caminho_arquivo)
        else:
            self.catalogo_de_produtos = CatalogoProdutosRepositoryMemory()
        
        self.registro = RegistradoraTest()
        # self.ui = UIConsoleAdapter(self.registro)
    
    def run(self):
        # self.ui.run()
        self.registro.test_inicial()

