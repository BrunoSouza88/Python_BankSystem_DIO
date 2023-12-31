def deposit(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def withdraw(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    try:
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def statement(extrato, saldo):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transaction in extrato:
            print(transaction)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def balance(saldo):
    print(f"\nSaldo atual: R$ {saldo:.2f}")


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[v] Saldo
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        saldo, extrato = deposit(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = withdraw(
            saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
    elif opcao == "e":
        statement(extrato, saldo)
    elif opcao == "v":
        balance(saldo)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente"
              " a operação desejada.")
