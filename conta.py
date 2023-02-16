class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Contruindo Objeto ...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print(f'Foi criado a seguinte conta:\nNumero: {self.__numero}\nTitular: {self.__titular}\nSaldo: R${self.__saldo:.2f}\nLimite: R${self.__limite:.2f}')

    def extrato(self):
        print(f'Titular: {self.__titular}\nExtrato: R${self.__saldo:.2f}')

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Titular: {self.__titular}\nDepósito: {valor:.2f}\nSaldo: R${self.__saldo:.2f}')

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'Titular: {self.__titular}\nFoi realizado um saque no valor de R${valor:.2f} \nSaldo: R${self.__saldo:.2f}')
        else:
            print(f'O valor R${valor} está acima do limite permitido.')
            print(f'Seu limite é de R${self.__limite}')

    def transferir(self, valor, destino):
        print('Iniciando transferência')
        print('')
        self.sacar(valor)
        print('')
        destino.depositar(valor)
        print('Transferência realizada com sucesso.')

    #Getters - Para Buscar
    @property
    def saldo(self):
        print(f'Segue o Saldo da conta: R${self.__saldo}')

    @property
    def titular(self):
        print(f'Segue o Titular da conta: {self.__titular}')

    @property
    def limite(self):
        print(f'Seu limite é de: R${self.__limite}')

    @property
    def info(self):
        print(f'Segue os dados do usuário:\nNumero: {self.__numero}\nTitular: {self.__titular}\nSaldo: R${self.__saldo:.2f}\nLimite: R${self.__limite:.2f}')

    #SET - Para alteração
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print(f'Seu limite R${self.__limite}')

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}