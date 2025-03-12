from ..core.services.VendaService import VendaService
from ..adapters.repositories.CatalogoProdutosRepositoryMemory import CatalogoProdutosRepositoryMemory
from ..core.entity.EspecificacaoProdutoEntity import EspecificacaoProdutoEntity
from .CatalogoProdutosTest import CatalogoProdutosTest

class VendaServiceTest:
    def __init__(self, catalogo_de_produtos: CatalogoProdutosTest):
        self.catalogo_de_produtos = catalogo_de_produtos
        self.venda_atual = None
    
    def servico_de_venda(self):
        catalogo = CatalogoProdutosRepositoryMemory()
        # Pré-carregando alguns produtos para teste
        catalogo.incluir_especificacao_produto(1, "Arroz", 10.50)
        catalogo.incluir_especificacao_produto(2, "Feijão", 7.99)
        catalogo.incluir_especificacao_produto(3, "Açúcar", 5.49)
        return VendaService(catalogo)
    
    def test_iniciar_nova_venda(self, servico_de_venda):
        # Teste para iniciar uma nova venda
        venda = servico_de_venda.iniciar_nova_venda()
        
        # Verificações
        assert venda is not None
        assert len(venda.itens_da_venda) == 0
    
    def test_adicionar_item_sem_venda_em_andamento(self, servico_de_venda):
        # Teste para adicionar item quando não há venda em andamento
        with pytest.raises(ValueError) as excinfo:
            servico_de_venda.adicionar_item_na_venda(1, 2)
        
        # Verifica se a mensagem de erro está correta
        assert "Nenhuma venda em andamento" in str(excinfo.value)
    
    def test_adicionar_item_com_quantidade_negativa(self, servico_de_venda):
        # Iniciar uma venda
        servico_de_venda.iniciar_nova_venda()
        
        # Teste para adicionar item com quantidade negativa
        with pytest.raises(ValueError) as excinfo:
            servico_de_venda.adicionar_item_na_venda(1, -3)
        
        # Verifica se a mensagem de erro está correta
        assert "A quantidade deve ser positiva" in str(excinfo.value)
    
    def test_adicionar_item_com_produto_inexistente(self, servico_de_venda, capsys):
        # Iniciar uma venda
        servico_de_venda.iniciar_nova_venda()
        
        # Teste para adicionar item com produto inexistente
        resultado = servico_de_venda.adicionar_item_na_venda(999, 2)
        
        # Verifica se retornou False (indicando que não foi adicionado)
        assert resultado is False
        
        # Verifica se a mensagem de aviso foi impressa
        capturado = capsys.readouterr()
        assert "Produto com ID 999 não encontrado" in capturado.out
    
    def test_adicionar_item_valido(self, servico_de_venda):
        # Iniciar uma venda
        servico_de_venda.iniciar_nova_venda()
        
        # Adicionar um item válido
        resultado = servico_de_venda.adicionar_item_na_venda(1, 3)
        
        # Verifica se retornou True (indicando sucesso)
        assert resultado is True
        
        # Verifica se o item foi adicionado à venda
        venda = servico_de_venda.obter_venda_atual()
        assert len(venda.itens_da_venda) == 1
        assert venda.itens_da_venda[0].quantidade == 3
        assert venda.itens_da_venda[0].especificacao_de_produto.id == 1
    
    def test_obter_total_da_venda_atual(self, monkeypatch, servico_de_venda):
        # Este teste usa monkeypatch para evitar os delays do Thread.sleep
        
        # Mock para o método get_price para evitar o sleep
        def mock_obter_preco(self):
            return self.preco
        
        # Mock para o método get_subtotal para evitar o sleep
        def mock_obter_subtotal(self):
            return self.quantidade * self.especificacao_de_produto.obter_preco()
        
        # Aplica os mocks
        monkeypatch.setattr(EspecificacaoProdutoEntity, "obter_preco", mock_obter_preco)
        
        # Iniciar uma venda e adicionar itens
        servico_de_venda.iniciar_nova_venda()
        servico_de_venda.adicionar_item_na_venda(1, 2)  # 2 x Arroz (10.50) = 21.00
        servico_de_venda.adicionar_item_na_venda(2, 3)  # 3 x Feijão (7.99) = 23.97
        
        # Calcular o total esperado
        total = servico_de_venda.obter_total_da_venda_atual()
        
        # O total esperado seria 21.00 + 23.97 = 44.97
        assert round(total, 2) == 44.97
    
    def test_finalizar_venda_com_pagamento_insuficiente(self, monkeypatch, servico_de_venda):
        # Mock para o método get_price para evitar o sleep
        def mock_obter_preco(self):
            return self.preco
        
        # Aplica o mock
        monkeypatch.setattr(EspecificacaoProdutoEntity, "obter_preco", mock_obter_preco)
        
        # Iniciar uma venda e adicionar itens
        servico_de_venda.iniciar_nova_venda()
        servico_de_venda.adicionar_item_na_venda(1, 2)  # 2 x Arroz (10.50) = 21.00
        
        # Tentar finalizar a venda com pagamento insuficiente
        with pytest.raises(ValueError) as excinfo:
            servico_de_venda.finalizar_venda(20.00)  # Pagamento menor que o total (21.00)
        
        # Verifica se a mensagem de erro está correta
        assert "Pagamento insuficiente" in str(excinfo.value)
    
    def test_finalizar_venda_sucesso(self, monkeypatch, servico_de_venda):
        # Mock para o método get_price para evitar o sleep
        def mock_obter_preco(self):
            return self.preco
        
        # Aplica o mock
        monkeypatch.setattr(EspecificacaoProdutoEntity, "obter_preco", mock_obter_preco)
        
        # Iniciar uma venda e adicionar itens
        servico_de_venda.iniciar_nova_venda()
        servico_de_venda.adicionar_item_na_venda(1, 1)  # 1 x Arroz (10.50) = 10.50
        
        # Finalizar a venda com sucesso
        troco = servico_de_venda.finalizar_venda(20.00)
        
        # O troco esperado seria 20.00 - 10.50 = 9.50
        assert troco == 9.50
