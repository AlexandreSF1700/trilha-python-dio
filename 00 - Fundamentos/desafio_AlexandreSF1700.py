menu = """
Qual operação deseja executar?

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

print('Bem vindo ao Banco XPTO!')
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'Operação de Depósito de R$ {valor:.2f} realizada com Sucesso!')

            while True:

                opcao2 = input('\nDeseja realizar outra Operação? (S/N): ')
                if opcao2 == "n" or opcao2 == "N" or opcao2 == "s" or opcao2 == "S":
                    break
                else:
                    print('O valor informado é inválido! Por favor responda corretamente a pergunta.')

            if opcao2 == "n" or opcao2 == "N":
                print('\nAgradecemos por utilizar o Banco XPTO.')
                break

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
            print(f'Operação de Saque de R$ {valor:.2f} realizada com Sucesso!')

            while True:

                opcao2 = input('\nDeseja realizar outra Operação? (S/N): ')
                if opcao2 == "n" or opcao2 == "N" or opcao2 == "s" or opcao2 == "S":
                    break
                else:
                    print('O valor informado é inválido! Por favor responda corretamente a pergunta.')

            if opcao2 == "n" or opcao2 == "N":
                print('\nAgradecemos por utilizar o Banco XPTO.')
                break

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

        while True:

            opcao2 = input('\nDeseja realizar outra Operação? (S/N): ')
            if opcao2 == "n" or opcao2 == "N" or opcao2 == "s" or opcao2 == "S":
                break
            else:
                print('O valor informado é inválido! Por favor responda corretamente a pergunta.')

        if opcao2 == "n" or opcao2 == "N":
            print('\nAgradecemos por utilizar o Banco XPTO.')
            break

    elif opcao == "q":
        print('\nAgradecemos por utilizar o Banco XPTO.')
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
