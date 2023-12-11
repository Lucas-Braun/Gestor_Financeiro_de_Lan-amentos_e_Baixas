"""
Nome do Projeto: Gestor Financeiro de Lançamentos e Baixas.

############### Lançamento de Conta a Pagar e Receber ###############

O programa permite a entrada de dados para contas a pagar e a receber.
São criados dois arquivos distintos para armazenar essas informações, um para contas a pagar e outro para contas a receber, facilitando a organização e o acesso aos dados.

############### Ver Extrato do Lançamento ###############

Os usuários podem visualizar um extrato dos lançamentos feitos.
O extrato inclui informações das contas a pagar e a receber, permitindo um acompanhamento eficiente das finanças.

############### Baixa dos Lançamentos ###############

A funcionalidade de baixa permite ao usuário selecionar uma conta específica (a pagar ou a receber) e registrar a sua liquidação.
Isso implica em marcar o lançamento escolhido como "Pago" ou "Recebido", atualizando o status da transação.

############### Sair do Programa ###############

Uma opção para encerrar o programa de forma segura, garantindo que todas as alterações feitas sejam salvas adequadamente.

"""
import pickle

def salvar_lancamentos(lancamentos, tipo):
    with open(f'{tipo}_lancamentos.pkl', 'wb') as arquivo:
        pickle.dump(lancamentos, arquivo)

def carregar_lancamentos(tipo):
    try:
        with open(f'{tipo}_lancamentos.pkl', 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return []

contas_a_pagar = carregar_lancamentos('pagar')
contas_a_receber = carregar_lancamentos('receber')

def processar_baixas(contas, tipo):
    if not contas:
        print(f'Não há contas a {tipo} para processar.')
        return

    for i, conta in enumerate(contas):
        print(f'{i + 1}. Valor: R${conta["valor"]}, Status: {conta["status"]}')

    try:
        escolha = int(input(f'Selecione a conta a {tipo} para dar baixa (1-{len(contas)}): '))
        if 1 <= escolha <= len(contas):
            if contas[escolha - 1]['status'] == 'Aberto':
                contas[escolha - 1]['status'] = 'Pago' if tipo == 'pagar' else 'Recebido'
                print(f'Baixa realizada com sucesso na conta {escolha}.')
            else:
                print('Esta conta já foi processada.')
        else:
            print('Seleção inválida.')
    except ValueError:
        print('Por favor, insira um número válido.')

while True:
    print('Escolha uma das opções:')
    print('1. Contas a Pagar')
    print('2. Contas a Receber')
    print('3. Baixas')
    print('4. Extrato')
    print('5. Sair')

    try:
        opcao = int(input('Insira a opção: '))
    except ValueError:
        print('Opção inválida. Insira um número de 1 a 5.')
        continue

    if opcao == 1:
        valor = float(input('Insira o valor da Conta a Pagar: '))
        contas_a_pagar.append({'valor': valor, 'status': 'Aberto'})
        print(f'Conta a Pagar de R${valor} adicionada com sucesso.')
        salvar_lancamentos(contas_a_pagar, 'pagar')

    elif opcao == 2:
        valor = float(input('Insira o valor da Conta a Receber: '))
        contas_a_receber.append({'valor': valor, 'status': 'Aberto'})
        print(f'Conta a Receber de R${valor} adicionada com sucesso.')
        salvar_lancamentos(contas_a_receber, 'receber')

    elif opcao == 3:
        print('Opção escolhida: Baixas')
        print('1. Baixa em Contas a Pagar')
        print('2. Baixa em Contas a Receber')
        try:
            escolha_baixa = int(input('Escolha o tipo de baixa (1-2): '))
            if escolha_baixa == 1:
                processar_baixas(contas_a_pagar, 'pagar')
                salvar_lancamentos(contas_a_pagar, 'pagar')
            elif escolha_baixa == 2:
                processar_baixas(contas_a_receber, 'receber')
                salvar_lancamentos(contas_a_receber, 'receber')
            else:
                print('Opção inválida.')
        except ValueError:
            print('Por favor, insira um número válido.')

    elif opcao == 4:
        print('Opção escolhida: Extrato')
        print('Contas a Pagar:')
        for i, conta in enumerate(contas_a_pagar):
            print(f'{i + 1}. Valor: R${conta["valor"]}, Status: {conta["status"]}')
        print('Contas a Receber:')
        for i, conta in enumerate(contas_a_receber):
            print(f'{i + 1}. Valor: R${conta["valor"]}, Status: {conta["status"]}')

    elif opcao == 5:
        print('Saindo do programa.')
        break

    else:
        print('Opção inválida. Insira um número de 1 a 5.')
