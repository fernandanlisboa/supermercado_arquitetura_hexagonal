import pytest
from ..core.entity.VendaEntity import VendaEntity
from ..core.entity.EspecificacaoProdutoEntity import EspecificacaoProduto

class VendaTest:
    
    @pytest.fixture
    def configurar_venda_com_produtos(self, monkeypatch):
        # Mock para o método get_price para evitar o sleep
        def mock_get_price(self):
            return self.preco
        
        # Aplica o mock
        monkeypatch.setattr(EspecificacaoProduto, "get_price", mock_get_price)
        
        # Cria uma venda e adiciona produtos
        venda = VendaEntity()
        
        # Cria especificações de produtos
        produto1 = EspecificacaoProduto(1, "Arroz", 10.50)
        produto2 = EspecificacaoProduto(2, "Feijão", 7.99)
        
        # Adiciona itens à venda
        venda.incluir_item(produto1, 2)  # 2 x Arroz (10.50) = 21.00
        venda.incluir_item(produto2, 1)  # 1 x Feijão (7.99) = 7.99
        
        return venda
    
    def test_obter_total(self, configurar_venda_com_produtos):
        # Obtém a venda configurada
        venda = configurar_venda_com_produtos
        
        # Calcula o total
        total = venda.obter_total()
        
        # O total esperado é 21.00 + 7.99 = 28.99
        assert round(total, 2) == 28.99
    
    def test_obter_troco(self, configurar_venda_com_produtos):
        # Obtém a venda configurada
        venda = configurar_venda_com_produtos
        
        # Calcula o troco para um pagamento de 50.00
        troco = venda.obter_troco(50.00)
        
        # O troco esperado é 50.00 - 28.99 = 21.01
        assert round(troco, 2) == 21.01
    
    def test_incluir_item(self):
        # Cria uma nova venda
        venda = VendaEntity()
        
        # Cria um produto
        produto = EspecificacaoProduto(3, "Açúcar", 5.49)
        
        # Adiciona o produto à venda
        venda.incluir_item(produto, 3)
        
        # Verifica se o item foi adicionado corretamente
        assert len(venda.itens_da_venda) == 1
        assert venda.itens_da_venda[0].quantidade == 3
        assert venda.itens_da_venda[0].especificacao_de_produto.id == 3
        assert venda.itens_da_venda[0].especificacao_de_produto.descricao == "Açúcar"
        assert venda.itens_da_venda[0].especificacao_de_produto.preco == 5.49
