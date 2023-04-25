""" Sistema bancario """

def menu():
    # Cria o menu.
    menu = """
    ==========================
     Informe a opção desejada 
    ==========================
    [d]  Depositar
    [s]  Sacar
    [t]  Transferencia
    [p]  Pagamento
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usúario
    [q]  Sair
    ==========================
    """

    # Retorna a opção escolhida.
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0: # Se for maior que 0.
        # Soma o valor do depósito no saldo.
        saldo += valor

        # Armazena o historico do depósito para o extrato.
        extrato += f"Depósito: R$ {valor:.2f}\n"

        # Informa que a operação foi realizada com sucesso.
        print("Depósito realizado com sucesso!")
    else: # Se form menor e igual a 0.
        # Valor do deposito e inválido.
        print("Operação falhou! O valor informado é inválido.")

    # retorna o resultado do deposito
    return saldo, extrato

def retirada(opcao, /, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Verifica se tem, saldo suficiente para sacar.
    excedeu_saldo = valor > saldo

    if excedeu_saldo: # Valor do saldo insuficiente, informa que o valor do saldo não e suficiente.
        print("Operação falhou! Saldo suficiente.")

    # Verifica se o valor limite para sque, foi excedido.
    excedeu_limite = valor > limite

    if excedeu_limite: # Valor do limite de saque maior de 500, informa que o valor de limite de saque foi excedido.
        print("Operação falhou! O valor excede o limite.")

    if opcao == "s": # Verifica se a operação e saque.
        # Verifica se o numero de saque foi exedido.
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saques: # Limite de saque maior que 3, informa que o limite de saque foi excedido.
            print("Operação falhou! Número máximo de saque excedido.")

    if valor > 0:
        # Diminui o saldo com o valor do saque·
        saldo -= valor

        if opcao == "s": mensagem = "Saque"
        elif opcao == "t": mensagem = "Tranferencia"
        elif opcao == "p": mensagem = "Pagamento"

        # Armazena o historico do saque para o extrato.
        extrato += mensagem + f": R$ {valor:.2f}\n"

        if opcao == "s": # Verifica se a operação e saque.
            # Adiciona mais um em limite de saque.
            numero_saques += 1

        # Informa que o saque foi realizado com sucesso·
        print("Operação relizada com sucesso!")

    else:
        # Informa que o valor informado e inválido
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    # Apresenta todas as movimentações na tela.
    print("\n============ EXTRATO ============")
    # Verifica se foi feita alguma movimentação, se caso nao tiver feito, informa que não tem movimento.
    print("Nao foram realizados movimentações." if not extrato else extrato)
    # mostra no final o saldo.
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=================================")

def criar_usuarios(usuarios):
    # Armazena o CPF informado.
    cpf = input("Informe o CPF (somente números): ")

    # Chama a função para verificar o cpf informado ja existe.
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: # Se caso o cpf exista.
        # Informa que o CPF ja existr. 
        print("Já existe usuário com esse CPF!")
        return

    # Solicita o nome do usuario e armazena.
    nome = input("Informe o nome completo: ")

    # Solicita a data de nascimento e armazena.
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    # Solcita o endereço (logradouro, número, bairro, cidade/sigla do estado) e armazena.
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): ")

    # Grava o usuário no diciánario.
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    # Informa que o usuário foi criado com sucesso.
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    # Verifica se o cpf informado ja existe, no dicionario usuarios.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    # se o cpf ja existir, retorna o primeiro resultado encontrado, se não existir, retorna none.
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    # Armazena o CPF informado.
    cpf = input("Informe o CPF do usuário:" )

    # Verifica se o usuário existe.
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: # Verifica se foi selecionado o usuario
        # Informa que a conta foi crida.
        print("Conta criada com sucesso!")

        # retorna a Agência, numero da conta, e usuario.
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    # Informa que o usuário não existe, e não cria a conta.
    print("Usuário não encontrado, fluxo de criação de conta encerrada!")

def listar_contas(contas):
    # Passa por todas as contas cadastradas.
    for conta in contas:
        # Monta a lista conta a conta.
        linha = f"""\
            =============== Lista Contas ===============
            Agência: " + {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            ============================================
        """
        # Apresente a lista com as contas cadastradas.
        print(linha)
            
def main():
    # Inicializa as variaveis.
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas =[]

    while True:
        # Chama função menu, e retorna a opção selecionada.
        opcao = menu()

        if opcao == "d": # Opção Deposito.
            # Informa o valor do depósito.
            valor = float(input("Informe o valor do depósito: "))
            
            # Chama função deposito, e retorna o saldo e extrato.
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s" or opcao == "t" or opcao == "p": # Opção "s" - Saque, Opção "t" - Transferencia, Opção "p" - Pagamento
            # Verifica qual a opção selecionada, para armazenar a mensagem referente a opção.
            if opcao == "s": mensagem = "do saque"
            elif opcao == "t": mensagem = "da tranferencia"
            elif opcao == "p": mensagem = "do pagamento"

            # Armazena o valor do saque, transferencia ou pagamento.
            valor = float(input("Informe o valor " + mensagem +": "))

            # Chama a função retirada (sacar, transferir ou pagamento), e retorna o saldo, extrato e o numero da quantidade de saque(numero_saque).
            saldo, extrato, numero_saques = retirada(
                opcao,
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e": # opção Extrato.
            # Chama a função extrato.
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc": # Opção nova conta.
            # Soma mais uma no numero da conta.
            numero_conta = len(contas) + 1
            
            # Chama a função nova conta.
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta: # Verifica se a conta ja existe.
                # Grava a conta no dicionário.
                contas.append(conta)

        elif opcao == "lc": # Opção listar contas.
            # Chama a função lista contas.
            listar_contas(contas)

        elif opcao == "nu": # Opção novo usúario.
            # Chama a função para criar usúario.
            criar_usuarios(usuarios)

        elif opcao == "q": # opção Fechar
            # Fecha o sistema.
            break

        else:
            # Informa que a opção escolhida e inválida, e pede para informar outra opção.
            print("Operação inválida, por favor selecione novamente a opção desejada.")

# Inicia o sistema.
main()
