def menu():
    menu = """\n
[1]\tdepositar
[2]\tsacar
[3]\textrato
[4]\tnova conta
[5]\tlistar contas
[6]\tnovo usuario
[7]\tsair
==>"""
    return input(menu)

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor 
        extrato +=f"depósito:\tR$ {valor:.2f}\n"
        print("\n#### depósito realizado com sucesso! ####")
    else:
        print("\n**** operação falhou, valor informado invalido! ****")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor >limite 
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n**** erro, voce não tem saldo suficiente. ****")

    elif excedeu_limite:
        print("\n**** erro, valor excede limite de valor de saque. ****")

    elif excedeu_saques:
        print("\n**** erro, limite de saque excedido. ****")

    elif valor > 0:
        saldo -= valor 
        extrato +=f"saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n#### saque realizado com sucesso! ####")

    else:
        print("\n****erro, operação nãorealizada ****")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n----------   extrato   ----------")
    print("nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nsaldo:\t\tR$ {saldo:.2f}")
    print("-------------------------------------")


def criar_usuario(usuarios):
    cpf = input("informe seu CPF (apenas numeros!):  ")
    usuario = filtar_usuario(cpf,usuarios)

    if usuario:
        print("\n**** este usuario ja esta cadastrado!  ****")
        return 
    nome = input("informe o nome completo: ")
    data_nascimento = input("insira seu aniversario(dia-mes-ano)")
    endereco = input("informe endereço: (logradouro, numero - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("#### usuario cadastrado com sucessso! #####")

def filtar_usuario(cpf, usuarios):
    usuarios_filtados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtados[0] if usuarios_filtados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o cpf do usuario: ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\n---- conta criada com sucesso! ----")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("#### usuario nao encontrado, criação de conta encerrada! ####")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        agencia:\t{conta['agencia']}
        c/c:\t\t{conta['numero_conta']}
        titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)


def main():
    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao =="1":
            valor = float(input("informe o valor do depósito:  "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("informe o valor do saque:  "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques, 
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break 
        else:
            print("**** operação invalida,por favor selecione a operação desejada novamente! ****")


main()