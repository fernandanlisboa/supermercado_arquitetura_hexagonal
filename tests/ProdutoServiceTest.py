import pytest
from ..core.services.ProdutoService import ProdutoService
from ..adapters.repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory
from .CatalogoProdutosTest import CatalogoProdutosTest

class ProdutoServiceTest:
    
    def __init__(self, catalogo_de_produtos: CatalogoProdutosTest):
        self.catalogo_de_produtos = catalogo_de_produtos
    
    @pytest.fixture
    def servico_de_produtos(self):
        catalogo = CatalogoProdutosRepositoryMemory()
        return ProdutoService(catalogo)
    
    def test_adicionar_produto_valido(self, servico_de_produtos):
        # Teste para adicionar um produto válido
        produto = servico_de_produtos.adicionar_produto(1, "Maçã", 5.99)
        
        # Verificações
        assert produto is not None
        assert produto.id == 1
        assert produto.descricao == "Maçã"
        assert produto.preco == 5.99
    
    def test_adicionar_produto_preco_negativo(self, servico_de_produtos):
        # Teste para verificar a validação de preço negativo
        with pytest.raises(ValueError) as excinfo:
            servico_de_produtos.adicionar_produto(2, "Laranja", -1.50)
        
        # Verifica se a mensagem de erro está correta
        assert "O preço do produto deve ser positivo" in str(excinfo.value)
    
    def test_adicionar_produto_descricao_vazia(self, servico_de_produtos):
        # Teste para verificar a validação de descrição vazia
        with pytest.raises(ValueError) as excinfo:
            servico_de_produtos.adicionar_produto(3, "", 7.25)
        
        # Verifica se a mensagem de erro está correta
        assert "A descrição do produto não pode estar vazia" in str(excinfo.value)
        
        # Teste com espaços em branco
        with pytest.raises(ValueError) as excinfo:
            servico_de_produtos.adicionar_produto(3, "   ", 7.25)
        
        assert "A descrição do produto não pode estar vazia" in str(excinfo.value)
    
    def test_adicionar_produto_id_negativo(self, servico_de_produtos):
        # Teste para verificar a validação de ID negativo
        with pytest.raises(ValueError) as excinfo:
            servico_de_produtos.adicionar_produto(-1, "Banana", 3.49)
        
        # Verifica se a mensagem de erro está correta
        assert "O ID do produto deve ser positivo" in str(excinfo.value)
    
    def test_obter_produto_inexistente(self, servico_de_produtos):
        # Teste para verificar o comportamento ao buscar um produto inexistente
        with pytest.raises(ValueError) as excinfo:
            servico_de_produtos.obter_produto(999)
        
        # Verifica se a mensagem de erro está correta
        assert "Produto com ID 999 não encontrado" in str(excinfo.value)
    
    def test_obter_produto_id_negativo(self, servico_de_produtos):
        # Teste para verificar a validação de ID negativo ao buscar um produto
        with pytest.raises(ValueError) as excinfo:
            servico_de_produtos.obter_produto(-5)
        
        # Verifica se a mensagem de erro está correta
        assert "O ID do produto deve ser positivo" in str(excinfo.value)
