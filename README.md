## Sistema de Cadastro de Clientes

Um sistema simples de cadastro de clientes desenvolvido em Python, utilizando o SQLite como banco de dados. Permite cadastrar, consultar, atualizar e excluir informações de clientes.

### Instalação

**Pré-requisitos:**

* Python 3.6 ou superior
* Bibliotecas: `sqlite3`, `sty`

**Clonar o repositório:**

```bash
git clone [https://github.com/seu_usuario/seu_repositorio.git](https://github.com/seu_usuario/seu_repositorio.git)
```
## Criar o banco de dados:

Ao executar o programa pela primeira vez, o banco de dados Cadastro.db será criado automaticamente, caso não exista.

## Executar o programa:

```bash python main.py```

# Como Usar

Ao iniciar o programa, você será apresentado a um menu interativo com as seguintes opções:

1. Ver lista de Clientes: Exibe todos os clientes cadastrados.
2. Ver cliente: Permite consultar as informações de um cliente específico, informando o ID.
3. Cadastrar novo cliente: Cadastra um novo cliente, solicitando nome, email, senha, telefone e CPF.
4. Deletar cliente: Exclui um cliente cadastrado, informando o ID.
5. Atualizar dados do cliente: Permite alterar os dados de um cliente, informando o ID e o campo a ser atualizado.
6. Sair: Encerra o programa.
   
## Estrutura do Projeto
* Databases: Contém as classes Banco e Repositorio, responsáveis pela interação com o banco de dados.
* Painel: Contém a classe Painel, que implementa a interface do usuário e as funcionalidades do sistema.
* trataDados: Contém funções auxiliares para validação e formatação de dados.
* main.py: Arquivo principal que inicia o programa.
