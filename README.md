# Supermercado Arquitetura Hexagonal

Este projeto é uma implementação de um sistema de caixa de supermercado utilizando a arquitetura hexagonal. O objetivo é praticar a aplicação dessa arquitetura na disciplina de Alta Qualidade de Software da Universidade SENAI CIMATEC, ministrada pelo professor Sergio Fernandes Martins.

Este fornece uma visão geral do projeto, incluindo sua estrutura, requisitos, instruções de instalação, execução, testes, contribuição, licença, autores e agradecimentos. Sinta-se à vontade para ajustá-lo conforme necessário.

<div align="center">
<img src="https://app.codacy.com/project/badge/Grade/d5c48b19966a4ada95b9c5706a5b6817" alt="Codacy Badge" />
</div>

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **adapters**: Contém os adaptadores que implementam as portas definidas no domínio. Inclui adaptadores para repositórios e interfaces de usuário.
  - **repositories**: Implementações de repositórios para persistência de dados.
  - **ui**: Implementações de interfaces de usuário.
- **application**: Contém a classe principal da aplicação que inicializa e configura os componentes do sistema.
- **core**: Contém o núcleo do domínio, incluindo entidades, portas e serviços.
  - **entity**: Modelos de domínio que representam os objetos do sistema.
  - **ports**: Interfaces que definem como o domínio se comunica com o mundo exterior.
  - **services**: Serviços que implementam as regras de negócio do sistema.
- **tests**: Contém os testes unitários e de integração para todos os componentes do sistema.

## Requisitos

- Python 3.8 ou superior
- pytest para execução dos testes

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/supermercado_arquitetura_hexagonal.git
   cd supermercado_arquitetura_hexagonal
    ```
2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
.\venv\Scripts\activate  # No Windows
source venv/bin/activate  # No Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução
Para executar a aplicação, utilize o seguinte comando:
```bash
python -m supermercado_arquitetura_hexagonal
```

## Testes
Para executar os testes, utilize o seguinte comando:
```bash
pytest
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Autores
- <img src="https://github.com/fernandanlisboa.png" width="20" height="20" style="border-radius: 50%;"> [Fernanda Lisboa](https://github.com/fernandanlisboa)
- <img src="https://github.com/Gustavo-Cruzz.png" width="20" height="20" style="border-radius: 50%;"> [Gustavo Cruz](https://github.com/Gustavo-Cruzz)
- <img src="https://github.com/Yas-bonfim.png" width="20" height="20" style="border-radius: 50%;"> [Yasmin Bonfim](https://github.com/Yas-bonfim)



## Agradecimentos
Agradecemos ao professor Sergio Fernandes Martins pela orientação e suporte durante o desenvolvimento deste projeto.

