from datetime import datetime

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular.title()
        self._saldo = saldo
        self._limite = limite
        data_hora = datetime.now()
        self._tempo = data_hora.strftime('%H:%M - %d/%m/%Y')
        print('CONTA SENDO CRIADA...')
        print(
            f'DADOS DA CONTA:\n\nNúmero da Conta: {self._numero}\nTitular: {self._titular}\nSaldo: R${self._saldo}\nLimite: R${self._limite}\nData da Criação: {self._tempo}')
        print(f'CONTA CRIADA COM SUCESSO\n')

    @property
    def info(self):
        return print(
            f'\nDADOS DA CONTA:\nNúmero da Conta: {self._numero}\nTitular: {self._titular}\nSaldo: R${self._saldo}\nLimite: R${self._limite}\n\nData da Criação: {self._tempo}\n')

    @property
    def numero(self):
        return print(f'\nNUMERO DA CONTA\nNúmero: {self._numero}\n')

    @numero.setter
    def numero(self, novo_numero):
        numero_antigo = self._numero
        self._numero = novo_numero
        print(f'\nATUALIZANDO NUMERO DA CONTA:\nNúmero Antigo: {numero_antigo}\nNovo Número: {self._numero}\n')

    @property
    def titular(self):
        return print(f'\nTITULAR DA CONTA:\nTitular: {self._titular}\n')

    @titular.setter
    def titular(self, novo_titular):
        titular_antigo = self._titular
        self._titular = novo_titular
        print(f'\nATUALIZAÇÃO DO NOME DO TITULAR:\nNome Antigo: {titular_antigo}\nNome Novo: {self._titular}\n')

    @property
    def saldo(self):
        return print(f'\nSALDO DA CONTA:\nSaldo: R${self._saldo}\n')


    def sacar(self, valor):
        print(f'INICIANDO SAQUE NA CONTA: {self._titular}')
        print(f'SALDO ATUAL: R${self._saldo}')
        print(f'LIMITE DA CONTA: R${self._limite}')
        if (self._saldo + self._limite) > valor:
            self._saldo -= valor
            print(f'FOI REALIZADO O SAQUE DE R${self._saldo}\n')
        else:
            print('SALDO INSUFICIENTE\n')


    def depositar(self, valor):
        print(f'INICIANDO SAQUE ...')
        print(f'SALDO ATUAL: R${self._saldo}')
        self._saldo += valor
        print(f'\nSALDO ATUALIZADO: R${self._saldo}\n')


    def transferir(self, origem, valor):
        print('INICIANDO TRANSFERÊNCIA ...')
        self._saldo -= valor
        self.origem = origem


conta1 = Conta('0001','Sergio',1000.0, 1000.0)
conta2 = Conta('0001','Yuri',1000.0, 1000.0)

conta1.sacar(500)
conta1.depositar(800)
conta1.info




