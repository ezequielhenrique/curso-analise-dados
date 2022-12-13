from BancoLib import Banco

print("========= Bem-vindo ao Banco UABJ =========")
bancoUfrpe = Banco("UABJ")

escolha = 1

while escolha > 0:
    print()
    print("------------- Menu -------------")
    print("0 - Sair")
    print("1 - Criar uma Nova Conta")
    print("2 - Consultar Saldo Conta")
    print("3 - Depositar na Conta")
    print("4 - Sacar na Conta")
    print("5 - Render Poupanca")
    print("6 - Render Bonus (Conta Bonificada)")
    print("--------------------------------")
    print()

    escolha = int(input("Digite a opção desejada: "))

    if escolha == 1:
        print("Criando Conta...")
        print("Escolha o tipo da conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))

        numConta = None
        if opcao == 1:
            numConta = bancoUfrpe.criarConta()
        elif opcao == 2:
            numConta = bancoUfrpe.criarPoupanca()
        elif opcao == 3:
            numConta = bancoUfrpe.criarContaBonificada()
        else:
            print("Entrada inválida, tente novamente!")

        if numConta != None:
            print("Conta criada:", numConta)

    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoUfrpe.consultaSaldo(numConta)

        if saldo == -1:
            print('A conta não existe')
        else:
            print("o saldo da conta", numConta, "é", saldo, "R$")

    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        deposito = bancoUfrpe.depositar(numConta, valor)

        if deposito:
            print("Valor Depositado")
        else:
            print('A conta não existe')

    elif escolha == 4:
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoUfrpe.sacar(numConta, valor)

        if resp:
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")

    elif escolha == 5:
        print("Rendendo Poupanca...")
        numConta = int(input("digite o numero da conta poupanca:"))
        resp = bancoUfrpe.renderPoupanca(numConta)

        if resp:
            print("Poupanca com novo saldo")
        else:
            print("A conta não é poupanca ou não existe")

    elif escolha == 6:
        print("Rendendo Bonus...")
        numConta = int(input("digite o numero da conta bonificada:"))
        resp = bancoUfrpe.renderBonus(numConta)

        if resp:
            print("Bonus da conta bonificada rendido")
        else:
            print("A conta não é bonificada ou não existe")


    elif escolha > 7:
        print("Entrada inválida, tente novamente!")

print("========== FIM DO PROGRAMA ==========")
