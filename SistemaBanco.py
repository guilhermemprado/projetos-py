""" Sistema bancario """

menu = """
[d] depositar
[s] Sacar
[t] transferencia
[p] pagaento
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

def validacao_operacoes(valor):
    autorizado = True

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saque = numero_saque >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Operação falhou! Você nao tem saldo suficiente.")
        return False
    
    elif excedeu_limite and (opcao == "s" or opcao == "t"):
        print("Operação falhou! O valor "if opcao == "s" "do saque" else "da transferencia"" excede o limite.")
        return False

    elif excedeu_saque and opcao == "s":
        print("Operação falhou! Número máximo de sques excedido.")
        return False
    
    else:
        # Pode seguir com a operaçao
        return True

while True:

    opcao = input(menu)
    
    if opcao == "d":
        """ Depósito """
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s" or opcao == "t" or opcao == "p":
        """ Saque, Transferencia e Pagamento """
        valor = float(input("Informe o valor: "))

        autorizou = validacao_operacoes(valor)

        if autorizou == True:
            if valor > 0:
                saldo -= valor
                if opcao == "s": # Saque
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saque += 1
                else: # Pagamento e tranferencia
                    if opcao =="p":
                        extrato += f"Pagamento: R$ {valor:.2f}\n"
                    else:
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
        