""" Sistema bancario """

menu = """
[d] depositar
[s] Sacar
[t] transferencia
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s" or opcao == "t":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você nao tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque and opcao == "s":
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            if opcao == "s":
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
            else: # Opçao transferencia
                extrato += f"Transferencia: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Nao foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")