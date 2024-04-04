# Desenvolver um sistema bancário básico que realize operações de depósito, saque e extrato.
# Depósito: deve ser sempre um valor positivo e todas as operações devem ser registradas no extrato.
# Saque: O sistema deve permitir apenas 3 saques diários com limite de R$500 por saque. O valor deve ser descontado do saldo. 
# Se o valor do saque for superior ao saldo, deve retornar uma mensagem de erro. Todas as operações devem ser registradas no extrato.
# Extrato: deve listar todos os depósitos e saques realizados na conta. Ao final da listagem, deve exibir o saldo.
# Caso o extrato esteja vazio, deve exibir a mensagem: "Não foram realizadas movimentações". Formato dos valores: R$ xxx.xx

SAQUES_DIARIOS = 3
LIMITE_SAQUE = 500
saldo = 0
movimentacoes = []
qtde_saques = 0

def deposito(valor, saldo):
    if valor > 0:
        saldo += valor
        movimentacoes.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('Valor inválido.')
        
    return saldo

def saque(valor, saldo):
    global qtde_saques
    if qtde_saques < SAQUES_DIARIOS:
        if valor <= saldo and valor <= LIMITE_SAQUE:
            saldo -= valor
            movimentacoes.append(f'Saque: R$ {valor:.2f}')
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')       
            qtde_saques += 1
            print(f'Saques diários restantes: {SAQUES_DIARIOS - qtde_saques}')
        elif valor > saldo:
            print('Saldo insuficiente.')
        elif valor > LIMITE_SAQUE:
            print('Valor excede o limite de R$ 500.')
    else:
        print('Limite de saques diários atingido.')
        
    return saldo

def extrato(saldo, movimentacoes):
    if len(movimentacoes) > 0:
        print(' Extrato: '.center(50, '-'))
        for movimentacao in movimentacoes:
            print(movimentacao)
        print(f'Saldo: R$ {saldo:.2f}')
    else:
        print('Não foram realizadas movimentações.')
        
while True:
    print(f"\n{'-'*50}")
    print(' Bem-vindo(a) ao PyBank '.center(50, '#'))
    opcao = input('Operações disponíveis \n1 - Depósito \n2 - Saque \n3 - Extrato \n4 - Sair \nEscolha a opção desejada: ')
    
    if opcao == '1':
        valor = float(input('Digite o valor do depósito: R$ '))
        saldo = deposito(valor, saldo)
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: R$ '))
        saldo = saque(valor, saldo)
    elif opcao == '3':
        extrato(saldo, movimentacoes)
    elif opcao == '4':
        print('Encerrando o sistema.')
        break
    else:
        print('Opção inválida.')