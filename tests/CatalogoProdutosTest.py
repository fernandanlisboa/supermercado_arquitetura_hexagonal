import pytest
from ..adapters.repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory

class CatalogoProdutosTest:
    
    @pytest.fixture
    def catalogo_de_produtos(self):
        catalogo = CatalogoProdutosRepositoryMemory()
        # Pré-carregando alguns produtos para teste
        catalogo.incluir_especificacao_produto(1, "Arroz", 10.50)
        catalogo.incluir_especificacao_produto(2, "Feijão", 7.99)
        catalogo.incluir_especificacao_produto(3, "Açúcar", 5.49)
        return catalogo
    
    def test_obter_especificacao_produto(self, catalogo_de_produtos):
        # Teste para verificar se conseguimos obter um produto específico
        produto = catalogo_de_produtos.obter_especificacao_produto(1)
        
        # Verificações
        assert produto is not None
        assert produto.id == 1
        assert produto.descricao == "Arroz"
        assert produto.preco == 10.50
    
    def test_incluir_especificacao_produto(self, catalogo_de_produtos):
        # Teste para verificar a inclusão de um novo produto
        catalogo_de_produtos.incluir_especificacao_produto(4, "Café", 12.75)
        
        # Verificar se o produto foi adicionado corretamente
        produto = catalogo_de_produtos.obter_especificacao_produto(4)
        
        # Verificações
        assert produto is not None
        assert produto.id == 4
        assert produto.descricao == "Café"
        assert produto.preco == 12.75
    
    def test_obter_produto_inexistente(self, catalogo_de_produtos):
        # Teste para verificar o comportamento ao buscar um produto que não existe
        produto = catalogo_de_produtos.obter_especificacao_produto(999)
        
        # Verificação: deveria retornar None para um produto inexistente
        assert produto is None
    
    def test_atualizar_produto(self, catalogo_de_produtos):
        # Teste para verificar a atualização (re-inclusão) de um produto existente
        catalogo_de_produtos.incluir_especificacao_produto(1, "Arroz Integral", 12.99)
        
        # Obter o produto atualizado
        produto = catalogo_de_produtos.obter_especificacao_produto(1)
        
        # Verificações
        assert produto is not None
        assert produto.id == 1
        assert produto.descricao == "Arroz Integral"
        assert produto.preco == 12.99
