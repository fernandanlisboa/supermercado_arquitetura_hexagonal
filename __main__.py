import argparse
from .application.CaixaSupermercadoMain import CaixaSupermercado
from .tests.CaixaSupermercadoTeste import CaixaSupermercadoTeste

def main():
    parser = argparse.ArgumentParser(description="Trabalho do modelo Hexagonal")
    parser.add_argument("-n", "--number", type=int, default=1, help="1 para executar testes, 0 para não")

    args = parser.parse_args()

    if args.number == 1:
        caixa = CaixaSupermercadoTeste(usar_catalogo_em_arquivo=False)
        # Executa a aplicação
        caixa.run()
    else:
        caixa = CaixaSupermercado(usar_catalogo_em_arquivo=True, caminho_arquivo="/home/gustavo/Downloads/hex_architecture_supermercado/produtos_spec.txt")
        # Executa a aplicação
        caixa.run()

if __name__ == "__main__":
    main()