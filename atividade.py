titular = "Joao Vitor Grella"
saldo = 500.00

# Controle do caixa eletrônico
caixa_com_cedulas = True

# Verifica se o caixa possui cédulas
if caixa_com_cedulas:

    print("=== Bem Vindo ===")
    print("1 - Ver Saldo")
    print("2 - Realizar Depósito")
    print("3 - Realizar Saque")
    print("4 - Simular Empréstimo")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":

        print(f"Cliente: {titular}")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":

        deposito = float(input("Digite o valor do depósito: R$ "))

        saldo += deposito

        print("Depósito concluído")
        print(f"Novo saldo: R$ {saldo:.2f}")


    elif opcao == "3":

        saque = float(input("Digite o valor do saque: R$ "))

        if saque > 0 and saque <= saldo:

            saldo -= saque

            print("Saque concluído")
            print(f"Novo saldo: R$ {saldo:.2f}")

        elif saque > saldo:

            print("Saldo insuficiente")

        else:

            print("Valor inválido")

   
    elif opcao == "4":

        limite = saldo * 3

        print(f"Seu limite estimado para empréstimo é de: R$ {limite:.2f}")

        emprestimo = float(input("Quanto deseja pegar emprestado? R$ "))

      
        if emprestimo <= limite and emprestimo < 5000:

            saldo += emprestimo

            print("✅ Empréstimo aprovado!")
            print(f"Novo saldo: R$ {saldo:.2f}")

        else:

            print("⚠️ Empréstimo recusado!")

  
    else:

        print("Opção inválida")
else:

    print("⚠️ Terminal em manutenção. Sem cédulas disponíveis.")
