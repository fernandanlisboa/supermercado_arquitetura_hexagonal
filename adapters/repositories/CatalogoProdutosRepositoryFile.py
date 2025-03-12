from ...core.ports.CatalogoProdutosPort import CatalogoProdutosPort
from ...core.entity.EspecificacaoProdutoEntity import EspecificacaoProdutoEntity
import pathlib

class CatalogoProdutosRepositoryFile(CatalogoProdutosPort):
    """Implementação baseada em arquivo da porta de catálogo de produtos"""
    
    def __init__(self, caminho_arquivo="../../produtos_spec.txt"):
        self.caminho_arquivo = pathlib.Path(caminho_arquivo)
        self.catalogo = {}
        self.carregar_catalogo()
    
    def carregar_catalogo(self):
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(',')
                    if len(partes) != 3:
                        print(f"Ignorando linha malformada: {linha}")
                        continue
                    
                    try:
                        id_ = int(partes[0])
                        descricao = partes[1]
                        preco = float(partes[2])
                        self.incluir_especificacao_produto(id_, descricao, preco)
                    except ValueError:
                        print(f"Ignorando linha malformada: {linha}")
        except IOError as e:
            print(f"Erro ao ler o arquivo: {e}")
    
    def obter_especificacao_produto(self, id_: int) -> EspecificacaoProdutoEntity:
        return self.catalogo.get(id_)
    
    def incluir_especificacao_produto(self, id_: int, descricao: str, preco: float) -> None:
        especificacao_produto = EspecificacaoProdutoEntity(id_, descricao, preco)
        self.catalogo[id_] = especificacao_produto