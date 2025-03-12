from ..adapters.repositories.CatalogoProdutosRepositoryFile import CatalogoProdutosRepositoryFile
from ..adapters.repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory
from ..adapters.RegistradoraAdapter import RegistradoraAdapter
from ..adapters.ui.UIConsoleAdapter import UIConsoleAdapter

class CaixaSupermercado:
    """Classe principal da aplicação"""
    
    def __init__(self, usar_catalogo_em_arquivo=True, caminho_arquivo="produtos_spec.txt"):
        if usar_catalogo_em_arquivo and caminho_arquivo:
            self.catalogo_de_produtos = CatalogoProdutosRepositoryFile(caminho_arquivo)
        else:
            self.catalogo_de_produtos = CatalogoProdutosRepositoryMemory()
        
        self.registro = RegistradoraAdapter(self.catalogo_de_produtos)
        self.ui = UIConsoleAdapter(self.registro)
    
    def run(self):
        self.ui.run()

