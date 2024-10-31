class Banco:
    import sqlite3

    def __init__(self, nome: str):
        self.__nome_banco = nome
        self.user: str = 'root'
        self.password: str = '12345'
        self._conn = self._conectar_banco()
        self._cursor_db = self._conn.cursor()
        self.logado: bool = False

    def _create_table(self):
        conn = self._conectar_banco()
        self._cursor_db.execute('''create table if not exists clientes(
        id integer primary key autoincrement,
        nome text not null,
        email text not null unique,
        senha text not null,
        data_criacao timestamp default current_timestamp,
        telefone text not null,
        cpf text unique not null
        )''')
        conn.commit()

    def desconectar_banco(self):
        close = self._conn.close()
        return close

    def _conectar_banco(self) -> any:
        try:
            conn = self.sqlite3.connect(self.__nome_banco)
            return conn
        except self.sqlite3.OperationalError as error:
            print(f'Erro ao se conectar com o banco de dados: {error}')
            return None


class Repositorio(Banco):
    def __init__(self, nome: str):
        super().__init__(nome)

    @staticmethod
    def __get_cpf(cpf) -> str:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    @staticmethod
    def __get_telefone(tel) -> str:
        return f'({tel[:2]}) {tel[3]} {tel[3:7]}-{tel[7:]}'

    def insert(self, nome: str, email: str, senha: str, telefone: str, cpf: str):
        if self._conn:
            self._create_table()
            try:
                query = '''INSERT INTO clientes (nome, email, senha, telefone, cpf) VALUES (?, ?, ?, ?, ?)'''
                self._cursor_db.execute(query, (nome, email, senha, telefone, cpf))
            except self.sqlite3.OperationalError as erro:
                print(f'Algo deu errado, código de erro: {erro}')
            finally:
                self._conn.commit()

    def select_all(self) -> str or list:
        if self._conn:
            self._create_table()
            dados_para_apresentar = list()
            try:
                resultado = self._cursor_db.execute('select * from clientes')
                for dado in resultado.fetchall():
                    dados_para_apresentar.append(dado)

                if not dados_para_apresentar:
                    return 'Nenhum cliente cadastrado'

                print(f"{'ID':<4} | {'Nome':<20} | {'Email':<25} | {'Telefone':<20} | {'CPF':<15} | {'Criação':^25} |")
                for dados in dados_para_apresentar:
                    print(f'{dados[0]:<4} | {dados[1]:<20} | {dados[2]:<25}'
                          f' | {self.__get_telefone(dados[5]):^20} | {self.__get_cpf(dados[6]):^15} | {dados[4]:^25} |')

            except self.sqlite3.OperationalError as erro:
                print(f'Algo deu errado, código de erro: {erro}')
            finally:
                dados_para_apresentar.clear()

    def select_especifico(self, identificador: str) -> str or list:
        if self._conn:
            self._create_table()
            try:
                resultado = self._cursor_db.execute(f'SELECT * FROM clientes WHERE id = ?', (identificador,))
                dado = resultado.fetchone()

                if dado is None:
                    return 'Nenhum cliente encontrado'

                return (f"{dado[0]:<4} | {dado[1]:<20} | {dado[2]:<25} | {self.__get_telefone(dado[5]):^20} | "
                        f"{self.__get_cpf(dado[6]):^15} | {dado[4]:^25}")

            except self.sqlite3.OperationalError as erro:
                print(f'Algo deu errado, código de erro: {erro}')

    def delete(self, identificador: int):
        if self._conn:
            self._create_table()
            try:
                self._cursor_db.execute(f'delete from clientes where id = {identificador}')
                print('Cliente deletado com sucesso')
            except self.sqlite3.OperationalError as erro:
                print(f'Algo deu errado, código de erro: {erro}')
            finally:
                self._conn.commit()

    def update(self, identificador: int, dado_a_ser_alterado: str, novo_dado: str):
        if self._conn:
            self._create_table()
            try:
                self._cursor_db.execute(f'update clientes set {dado_a_ser_alterado} = {novo_dado}'
                                        f' where id = {identificador}')
                print(f'{dado_a_ser_alterado} alterado com sucesso para {novo_dado}')
            except self.sqlite3.OperationalError as erro:
                print(f'Algo deu errado, código de erro: {erro}')
            finally:
                self._conn.commit()

    def validar_email(self, email: str) -> bool:
        lista_dados_temporarea = list()
        for i in self.select_all():
            lista_dados_temporarea.append(i)
        if lista_dados_temporarea[2] == email:
            lista_dados_temporarea.clear()
            return False
        else:
            lista_dados_temporarea.clear()
            return True

    def validar_cpf(self, cpf: str) -> bool:
        dados_temporaries = list()
        for i in self.select_all():
            dados_temporaries.append(i)

        if dados_temporaries[4] == cpf:
            dados_temporaries.clear()
            return False
        else:
            dados_temporaries.clear()
            return True

    def acessar(self):
        if self.logado is False:
            import tkinter as tk
            from tkinter import messagebox

            def on_login():
                username = entry_username.get()
                password = entry_password.get()

                # Verificação das credenciais
                if username == self.user and password == self.password:
                    messagebox.showinfo("Login Info", "Login bem-sucedido!")
                    root.destroy()
                    self.logado = True
                else:
                    messagebox.showerror("Erro de Login", "Usuário ou Senha incorretos.")
                    self.logado = False

            root = tk.Tk()
            root.title("Tela de Login")
            root.geometry("400x250")

            tk.Label(root, text="Usuário").pack(pady=10)
            entry_username = tk.Entry(root)
            entry_username.pack(pady=10)

            tk.Label(root, text="Senha").pack(pady=10)
            entry_password = tk.Entry(root, show='*')
            entry_password.pack(pady=10)

            button = tk.Button(root, text="Login", command=on_login)
            button.pack(pady=25)

            root.mainloop()

    def validar_senha(self, senha_antiga: str, identifier) -> bool:
        try:
            senha_bd = self._cursor_db.execute(f'select senha from clientes where id = {identifier}').fetchone()[0]
            if senha_bd == senha_antiga:
                return True
            else:
                return False
        except self.sqlite3.OperationalError as erro:
            print(f'Erro ao consultar senha: {erro}')
