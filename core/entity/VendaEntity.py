import datetime
import time
from .ItemDeVendaEntity import ItemDeVendaEntity
from .EspecificacaoProdutoEntity import EspecificacaoProdutoEntity

class VendaEntity:
    """Modelo de domínio para uma venda"""
    
    def __init__(self):
        self.itens_de_venda = []
        self.data_hora = datetime.datetime.now()
    
    def incluir_item(self, especificacao_produto: EspecificacaoProdutoEntity, quantidade: int):
        self.itens_de_venda.append(ItemDeVendaEntity(especificacao_produto, quantidade))
    
    def get_total(self):
        total = 0.0
        print(f"Total: {total}")
        time.sleep(1)  # Simulando o Thread.sleep(1000) do Java
        for item in self.itens_de_venda:    
        #     print(item.get_subtotal())      
        #     total += item.get_subtotal()
        # print(total)
        # return total
            return item.get_subtotal()
    
    def get_troco(self, valor_pago: float):
        troco = valor_pago - self.get_total()
        return round(troco, 2)
