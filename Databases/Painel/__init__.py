from .Banco import Repositorio
from .trataDados import *
from sty import fg


class Painel:

    def __init__(self, banco_de_dados: str):
        self.banco = Repositorio(banco_de_dados)

    @staticmethod
    def cor_terminal(msg, cor):
        return cor + msg + fg.rs

    def exibir_painel(self):
        while True:
            self.__painel()

    def __painel(self):
        self.tamanho = 130
        print('=' * self.tamanho)
        print(f'{self.cor_terminal("Cadastrar Clientes", fg.white):^{self.tamanho}}')
        print('=' * self.tamanho)
        print(f'{self.cor_terminal("1", fg.red)} - {self.cor_terminal("Ver lista de Clientes", fg.blue)}')
        print(f'{self.cor_terminal("2", fg.red)} - {self.cor_terminal("Ver cliente", fg.blue)}')
        print(f'{self.cor_terminal("3", fg.red)} - {self.cor_terminal("Cadastrar novo cliente", fg.blue)}')
        print(f'{self.cor_terminal("4", fg.red)} - {self.cor_terminal("Deletar cliente", fg.blue)}')
        print(f'{self.cor_terminal("5", fg.red)} - {self.cor_terminal("Atualizar dados do cliente", fg.blue)}')
        print(f'{self.cor_terminal("6", fg.red)} - {self.cor_terminal("Sair", fg.blue)}')
        self.__option(self.cor_terminal('Sua opção: ', fg.grey))


    def __option(self, inp: str) -> None:
        opt = validar_entrada(inp)
        if opt == 1:
            print(self.banco.select_all())
        elif opt == 2:
            identificador = validar_num_inteiro('Digite o ID do cliente que deseja ver: ')
            print(self.banco.select_especifico(identificador))
        elif opt == 3:
            self.banco.acessar()
            if self.banco.logado:
                nome = str(input('Nome: '))
                email = str(input('E-mail: '))
                while True:
                    if validar_final_email(email) is False:
                        email = str(input('Digite um email válido: '))
                    else:
                        break
                if self.banco.validar_email(email) is False:
                    print('Este Email já está cadastrado')
                    return
                senha = str(input('Digite sua senha: '))
                senha = validar_tamanho_da_senha(senha)
                confirm_senha = str(input('Confirmar senha: '))
                while True:
                    if confirm_pass(senha, confirm_senha) is False:
                        confirm_senha = str(input('Digite a senha novamente: '))
                    else:
                        break
                cpf = str(input('CPF: '))
                while True:
                    if validar_tamanho_do_cpf(cpf) is False:
                        cpf = str(input('Digite um cpf válido: '))
                    else:
                        break
                if self.banco.validar_cpf(cpf) is False:
                    print('Este cpf já está cadastrado')
                    return
                cpf = formatar_cpf_para_o_banco(cpf)

                telefone = str(input('Telefone: '))
                while True:
                    if ler_tamanho_telefone(telefone) is False:
                        print('Digite o número de telefone com o DDD (exemplo: (11) 9 9999-9999)')
                        telefone = str(input('Telefone: '))
                    else:
                        break
                telefone = formatar_telefone_para_o_banco(telefone)
                self.banco.insert(nome, email, senha, telefone, cpf)
            else:
                return 'Você não tem permissão para esta ação'
        elif opt == 4:
            self.banco.acessar()
            if self.banco.logado:
                identifier = validar_num_inteiro('Digite o ID do cliente que deseja deletar: ')
                self.banco.delete(identifier)
            else:
                return 'Você não tem permissão para esta ação'
        elif opt == 5:
            self.banco.acessar()
            if self.banco.logado:
                identifier = validar_num_inteiro('Digite o ID do cliente que deseja atualizar: ')
                self.__dados_para_update(identifier)
                if self.continuar_para_update:
                    self.banco.update(identifier, self.alter_dado, self.novo_dado)
            else:
                return 'Você não tem permissão para esta ação'
        elif opt == 6:
            print('saindo...')
            self.banco.desconectar_banco()
            quit()

    def __dados_para_update(self, identifier: int) -> None:
        print('=' * self.tamanho)
        print(f"{'Atualizar dados do cliente':^{self.tamanho}}")
        print('=' * self.tamanho)
        print('1 - Nome')
        print('2 - Telefone')
        print('3 - Senha')
        print('4 - Voltar')
        self.__option_update('sua opção: ', identifier)

    def __option_update(self, inpt, identifier) -> None:
        self.continuar_para_update = True
        opt = validar_entrada_update(inpt)
        if opt == 1:
            self.novo_dado = str(input('Novo nome: '))
            self.alter_dado = 'nome'
        elif opt == 2:
            nv_telefone = str(input('Novo telefone: '))
            while ler_tamanho_telefone(nv_telefone) is False:
                print('Digite o número de telefone com o DDD (exemplo: (11) 9 9999-9999)')
                nv_telefone = str(input('Telefone: '))
            nv_telefone = formatar_telefone_para_o_banco(nv_telefone)
            self.novo_dado = nv_telefone
            self.alter_dado = 'telefone'
        elif opt == 3:
            senha_antiga = str(input('Senha antiga: '))
            while True:
                if self.banco.validar_senha(senha_antiga, identifier) is False:
                    senha_antiga = str(input('Senha incorreta\nDigite a senha antiga novamente: '))
                else:
                    break
            nv_senha = str(input('Nova senha: '))
            nv_senha = validar_tamanho_da_senha(nv_senha)
            self.novo_dado = nv_senha
            self.alter_dado = 'senha'
        elif opt == 4:
            self.continuar_para_update = False
            return 'Voltando...'
