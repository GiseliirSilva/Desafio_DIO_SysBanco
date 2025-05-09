# Sistema Bancário em Python - Projeto DIO

Este projeto implementa um sistema bancário simples com as operações de depósito, saque e extrato, conforme solicitado no Bootcamp Suzano - Python Developer da Digital Innovation One (DIO).

## Implementação Desenvolvida

Este repositório contém a implementação do sistema bancário que desenvolvi, com as seguintes características:

* As operações de depósito, saque e extrato foram modularizadas em funções separadas para melhor organização e reutilização do código.
* A função de saque implementa as restrições de limite de valor por saque e limite diário de saques, além de verificar o saldo disponível.
* A função de extrato exibe todas as movimentações e o saldo atual da conta, formatados em moeda brasileira (R$ XXX.XX).

Você pode encontrar o código completo desta implementação no arquivo `banco.py`.

## Código Original Fornecido para elaboração do DESAFIO

Abaixo está o código original fornecido durante o curso como base para a implementação do sistema bancário:

```python
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
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
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
