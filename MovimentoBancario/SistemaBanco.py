import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        """ Inicializa as variaveis """
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        """ Saldo """
        return self._saldo

    @property
    def numero(self):
        """ Número da conta """
        return self._numero

    @property
    def agencia(self):
        """ Agência """
        return self._agencia

    @property
    def cliente(self):
        """ Cliente """
        return self._cliente

    @property
    def historico(self):
        """ Hitórico de operações """
        return self._historico

    def sacar(self, valor):
        """ Sacar """
        # Armazena o saldo.
        saldo = self.saldo
        # Verifica se o valor da operação e maior que o saldo.
        excedeu_saldo = valor > saldo

        # Verifica se o usuario tem saldo suficiente.
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        # Verifica se o valor da operação e mais que 0.
        elif valor > 0:
            # Retira do saldo o valor da operação.
            self._saldo -= valor
            # Informa que a operação foi realizada com sucesso.
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            # Informa que a operação falhou, pois o valor informado e inválido.
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
    
    def transferir(self, valor):
        """ Transferir """
        # Armazena o saldo.
        saldo = self.saldo
        # Verifica se o valor da operação e maior que o saldo.
        excedeu_saldo = valor > saldo

        # Verifica se o usuario tem saldo suficiente.
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        # Verifica se o valor da operação e mais que 0.
        elif valor > 0:
            # Retira do saldo o valor da operação.
            self._saldo -= valor
            # Informa que a operação foi realizada com sucesso.
            print("\n=== Transferência realizado com sucesso! ===")
            return True

        else:
            # Informa que a operação falhou, pois o valor informado e inválido.
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def pagamento(self, valor):
        """ Pagamento """
        # Armazena o saldo.
        saldo = self.saldo
        # Verifica se o valor da operação e maior que o saldo.
        excedeu_saldo = valor > saldo

        # Verifica se o usuario tem saldo suficiente.
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        # Verifica se o valor da operação e mais que 0.
        elif valor > 0:
            # Retira do saldo o valor da operação.
            self._saldo -= valor
            # Informa que a operação foi realizada com sucesso.
            print("\n=== Pagamento realizado com sucesso! ===")
            return True

        else:
            # Informa que a operação falhou, pois o valor informado e inválido.
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        """ Depositar """
        # Verifica se o valor da operação e mais que 0.
        if valor > 0:
            # Soma o valor da operação ao valor do saldo.
            self._saldo += valor
            # Informa que a operação foi realizada com sucesso.
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            # Informa que a operação falhou, pois o valor informado e inválido.
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        # Inicializa o dicionario.
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Grava os valores (transação, valor e data) no dicionario transações.
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        # Armazena o valor do saque.
        self._valor = valor

    @property
    def valor(self):
        # Retorna o valor.
        return self._valor

    def registrar(self, conta):
        # Chama conta.sacar.
        sucesso_transacao = conta.sacar(self.valor)

        # Verifica se a operação foi realzada com sucesso.
        if sucesso_transacao:
            # Regista no historico o sucesso da operação.
            conta.historico.adicionar_transacao(self)

class Transferencia(Transacao):
    def __init__(self, valor):
        # Armazena o valor do transferencia.
        self._valor = valor

    @property
    def valor(self):
        # Retorna o valor.
        return self._valor

    def registrar(self, conta):
        # Chama a conta.transferir.
        sucesso_transacao = conta.transferir(self.valor)

        # Verifica se a operação foi realzada com sucesso.
        if sucesso_transacao:
            # Regista no historico o sucesso da operação.
            conta.historico.adicionar_transacao(self)

class Pagamento(Transacao):
    def __init__(self, valor):
        # Armazena o valor do pagamento.
        self._valor = valor

    @property
    def valor(self):
        # Retorna o valor.
        return self._valor

    def registrar(self, conta):
        # Chama a conta.pagamento
        sucesso_transacao = conta.pagamento(self.valor)

        # Verifica se a operação foi realzada com sucesso.
        if sucesso_transacao:
            # Regista no historico o sucesso da operação.
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        # Armazena o valor do depósito.
        self._valor = valor

    @property
    def valor(self):
        #retorna o valor.
        return self._valor

    def registrar(self, conta):
        # Registra aoperação.
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            # Grava no histórico a operação efetuada.
            conta.historico.adicionar_transacao(self)

def menu(clientes, contas):
    """ Monta e apresenta menu """
    # Verifica se tem usuário, e mostra somente novo usuario e sair.
    if clientes == 0:
        menu = """\n
        ================ MENU ================
        [nu] Novo usuário
        [q]  Sair
        => """
    
    # Se tem usuário e não tem conta, mostra somente menu parcial.
    elif clientes > 0 and contas == 0:
        menu = """\n
        ================ MENU ================
        [nc] Nova conta
        [nu] Novo usuário
        [q]  Sair
        => """

    # Se tem usuário e conta, mostra todo o menu.
    else:
        menu = """\n
        ================ MENU ================
        [d]  Depositar
        [s]  Sacar
        [t]  Transferência
        [p]  Pagamento
        [e]  Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q]  Sair
        => """

    # Retorna o menu.
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    """ Verifica se o cliente ja existe """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    """ Verifica se o cliente tem conta """
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    """ Depósito """
    # Armazena o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")

    # Consulta o cliente.
    cliente = filtrar_cliente(cpf, clientes)

    # Verifica se o cliente ja existe.
    if not cliente:
        # Informa que o cliente não existe.
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Armazena o valor do depósito.
    valor = float(input("Informe o valor do depósito: "))
    # Valida o depósito.
    transacao = Deposito(valor)

    # Busca a conta do cliente.
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a operação.
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    # Armazena o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")
    # Consulta o cliente.
    cliente = filtrar_cliente(cpf, clientes)

    # Verifica se o cliente ja existe.
    if not cliente:
        # Informa que o cliente não existe.
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Armazena o valor do depósito.
    valor = float(input("Informe o valor do saque: "))
    # Valida o depósito.
    transacao = Saque(valor)

    # Busca a conta do cliente.
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a operação.
    cliente.realizar_transacao(conta, transacao)

def transferir(clientes):
    # Armazena o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")
    # Verifica se o cliente ja existe.
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        # Informa que o cliente não existe.
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Armazena o valor do depósito.
    valor = float(input("Informe o valor da transferência: "))
    # Valida o depósito.
    transacao = Transferencia(valor)

    # Busca a conta do cliente.
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a operação.
    cliente.realizar_transacao(conta, transacao)

def pagamento(clientes):
    # Armazena o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")
    # Consulta o cliente.
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        # Informa que o cliente não existe.
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Armazena o valor do depósito.
    valor = float(input("Informe o valor do pagamento: "))
    # Valida o depósito.
    transacao = Pagamento(valor)

    # Busca a conta do cliente.
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a operação.
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    # Armazena o CPF do cliente.
    cpf = input("Informe o CPF do cliente: ")
    # Consulta o cliente.
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        # Informa que o cliente não existe.
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Busca a conta do cliente.
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Monta extrato, com todos os operações do histórico para apresentar
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    # Armazena o CPF do cliente.
    cpf = input("Informe o CPF (somente número): ")
    # Consulta o cliente.
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        # Informa que o cliente não existe.
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    # Armazena o nome do cliente.
    nome = input("Informe o nome completo: ")
    # Armazena a data de nascimento.
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    # Armazena o endereço completo (logradouro, nro - bairro - cidade/sigla estado).
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    # Grava o cliente.
    clientes.append(cliente)

    # Informa que o clliente foi criado com sucesso.
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    """ Cria conta """
    # Armazena cpf do cliente.
    cpf = input("Informe o CPF do cliente: ")
    # Verifica se o cliente existe.
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        # informa que o cliente não existe, e encerra operação.
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # Armazena o numero da conta.
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    # Grava a conta.
    contas.append(conta)
    # Grava vincula a conta ao cliente.
    cliente.contas.append(conta)

    # Informa que a conta foi criada com sucesso.
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    """ Lista de contas """
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    # Inicializa dicionários.
    clientes = []
    contas = []

    while True:
        # Armazena qual a opção selecionada.
        opcao = menu(len(clientes), len(contas))

        if opcao == "d": # Depósito.
            depositar(clientes)

        elif opcao == "s": # Saque.
            sacar(clientes)

        elif opcao == "t": # Transferência.
            transferir(clientes)

        elif opcao == "p": # Pagamento.
            pagamento(clientes)

        elif opcao == "e": # Extrato.
            exibir_extrato(clientes)

        elif opcao == "nu": # Novo usuário.
            criar_cliente(clientes)

        elif opcao == "nc": # Nova conta.
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc": # Lista Contas.
            listar_contas(contas)

        elif opcao == "q": # Sair.
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

main()
