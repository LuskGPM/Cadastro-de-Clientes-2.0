def formatar_cpf_para_o_banco(cpf) -> str:
    cpf_alter = cpf.replace('.', '').replace('-', '')
    cpf_alter = cpf_alter.strip()
    return cpf_alter


def formatar_telefone_para_o_banco(tel) -> str:
    tel_alter = tel.replace('-', '').replace('(', '').replace(')', '')
    tel_alter = tel_alter.strip()
    return tel_alter


def validar_tamanho_do_cpf(cpf) -> bool:
    cpf = cpf.replace('.', '').replace('-', '')
    cpf = cpf.strip()
    if len(cpf) != 11:
        return False
    else:
        return True


def ler_tamanho_telefone(tel) -> bool:
    tel_alter = tel.replace('-', '').replace('(', '').replace(')', '')
    tel_alter = tel_alter.strip()
    if len(tel_alter) == 11:
        return True
    elif len(tel_alter) < 11:
        return False




def validar_num_inteiro(input_n: str) -> int:
    while True:
        try:
            num = int(input(input_n))
            return num
        except ValueError:
            print('Digite um número inteiro válido')


def validar_entrada(entrada: str) -> int:
    valor = validar_num_inteiro(entrada)
    while 1 > valor > 6:
        print('Digite um número correspondente ás escolhas acima')
        valor = validar_num_inteiro(entrada)
    return valor


def validar_final_email(email) -> bool:
    return email.strip().lower().endswith(
        (
            '@gmail.com',
            '@hotmail.com',
            '@outlook.com',
            '@yahoo.com.br'
        )
    )


def confirm_pass(senha, conf_senha) -> bool:
    if senha == conf_senha:
        return True
    else:
        return False


def validar_entrada_update(entrada: str):
    valor = validar_num_inteiro(entrada)
    while 1 > valor > 4:
        print('Digite um número correspondente ás escolhas acima')
        valor = validar_num_inteiro(entrada)
    return valor


def validar_tamanho_da_senha(senha) -> bool:
    try:
        if len(senha) < 8:
            print('A senha deve conter mais de 8 caracteres')
            return False
        else:
            return True
    except TypeError as erro:
        print(f'Erro ao ler número de caracteres da senha: {erro}')
        return False
