# Sistema bancário simples

# Fução Depositar:


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato


# Função Saque:


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite diário de sáques atingido.")
        return saldo, extrato, numero_saques
    if valor > limite:
        print("O valor máximo por saque é de R$ {limite:.2f}.")
        return saldo, extrato, numero_saques
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato, numero_saques
    if valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        return saldo, extrato, numero_saques
    else:
        print("O valor do saque deve ser positivo.")
        return saldo, extrato, numero_saques


# Função extrato:


def exibir_extrato(saldo, extrato):
    print("\n ============ EXTRATO ============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato, end="")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================")


def main():
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = input(
            "\nSelecione a operação desejada:\n"
            "[1] Depositar\n"
            "[2] Sacar\n"
            "[3] Extrato\n"
            "[4] Sair\n=> "
        )

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print(
                "Opção inválida. Por favor, selecione uma das "
                "opções listadas."
            )


if __name__ == "__main__":
    main()
