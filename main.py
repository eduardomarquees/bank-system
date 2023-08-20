class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, nome, saldo_inicial):
        if numero_conta in self.contas:
            print('Conta já existente')
        else:
            self.contas[numero_conta] ={
                "nome": nome,
                "saldo": saldo_inicial
            }
            print('Conta criada com sucesso')

    def depositar(self, numero_conta, saldo):
        if numero_conta in self.contas:
            self.contas[numero_conta]["saldo"] += saldo
            print('Deposito realizado com sucesso')
        else:
            print('Conta não encontrada')

    def sacar(self, numero_conta, saldo):
        if numero_conta in self.contas:
            if self.contas[numero_conta]["saldo"] >= saldo:
                self.contas[numero_conta]["saldo"] -= saldo
                print('Saque realizado com sucesso')
            else:
                print('Saldo não sucifiente')
        else:
            print('Conta não encontrada')

    def chechar_saldo(self, numero_conta):
        if numero_conta in self.contas:
            print(f"Saldo disponivível: {self.contas[numero_conta]['saldo']}")
        else:
            print('Conta não encontrada')

banco = Banco()

while True:
    print("\n========== BANCO BEM SIMPLES ==========")
    print('1. Criar Conta')
    print('2. Realizar deposito')
    print('3. Realizar saque')
    print('4. Verficicar saldo')
    print('5. Sair')

    opcoes = input('Esolha uma opção: ')

    if opcoes == '1':
        numero_conta = input('Digite o número da conta: ')
        nome = input('Digite o nome do titular da conta: ')
        saldo_inicial = float(input('Digite o valor inicial da conta: '))
        banco.criar_conta(numero_conta, nome, saldo_inicial)
    elif opcoes == '2':
        numero_conta = input('Digite o número da conta: ')
        saldo = float(input('Digite o valor a ser depositado: '))
        banco.depositar(numero_conta, saldo)
    elif opcoes == '3':
        numero_conta = input('Digite o número da conta: ')
        saldo = float(input('Digite o valor a ser sacado: '))
        banco.sacar(numero_conta, saldo)
    elif opcoes == '4':
        numero_conta = input('Digite o número da conta: ')
        banco.chechar_saldo(numero_conta)
    elif opcoes == '5':
        print('Saindo do sistema')
        break
    else:
        print('Opção invalida, tente uma opção valida!')