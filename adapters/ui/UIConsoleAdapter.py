from ...core.ports.UIPort import UIPort
from ..RegistradoraAdapter import RegistradoraAdapter

class UIConsoleAdapter(UIPort):
    """Console implementation of the UI port"""
    
    def __init__(self, register: RegistradoraAdapter):
        self.register = register
    
    def run(self) -> None:
        self.construir_catalogo_produtos()
        
        terminate = False
        while not terminate:
            print("Select 1 for new sale, 2 to exit")
            try:
                option = int(input())
                if option == 1:
                    self.iniciar_venda()
                elif option == 2:
                    print("Adeus")
                    terminate = True
                else:
                    print("Opção inválida")
            except ValueError:
                print("Input inválido")
    
    def construir_catalogo_produtos(self) -> None:
        try:
            # This is simplified to match the Java implementation
            # In a real application, you might want to use a more flexible approach
            for i, (description, price) in enumerate([
                ("Product 1", 8.97),
                ("Product 2", 0.0),  # This wasn't in the Java code, just an example
                ("Product 3", 0.0),  # This wasn't in the Java code, just an example
                ("Product 4", 0.0)   # This wasn't in the Java code, just an example
            ], 1):
                self.register.incluir_especificacao_produto(i, description, price)
            
            # Print some products to show they were loaded
            catalog = self.register.get_catalogo_produtos()
            print("Lendo arquivo...")
            for i in range(1, 5):
                product_spec = catalog.obter_especificacao_produto(i)
                if product_spec:
                    print(product_spec)
        except Exception as e:
            print(f"Erro ao criar catálogo: {e}")
    
    def iniciar_venda(self) -> None:
        self.register.iniciar_venda()
        end_sale = False
        
        while not end_sale:
            print("Type 1 to include product; 2 to finish sale")
            try:
                option = int(input())
                if option == 1:
                    print("Digite o código do produto")
                    product_id = int(input())
                    print("Digite a quantidade")
                    quantity = int(input())
                    self.register.incluir_item(product_id, quantity)
                elif option == 2:
                    total = self.register.get_total()
                    print(f"Total da venda: {total}")
                    print("Digite o valor pago")
                    amount_paid = float(input())
                    print(f"Change = {self.register.get_troco(amount_paid)}")
                    end_sale = True
                else:
                    print("Opção inválida")
            except ValueError:
                print("Input inválido")