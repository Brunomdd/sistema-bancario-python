#Enunciado – Sistema Bancário V1
#Desenvolva um programa em Python que simule um sistema bancário simples, utilizando funções, listas, dicionários e menu interativo.
#O sistema deve manter uma lista de contas bancárias, onde cada conta possui:
#número da conta
#nome do titular
#saldo
#status de ativação
#O programa deve exibir um menu principal e permitir ao usuário escolher uma das opções disponíveis.
#📋 Funcionalidades do sistema
#1️⃣ Listar contas
#Exibir o nome do titular e o saldo de todas as contas cadastradas.
#2️⃣ Transferência entre contas
#Solicitar:
#número da conta de origem
#número da conta de destino
#valor da transferência
#Regras:
#o valor deve ser maior que zero
#as contas devem existir
#não é permitido transferir para a mesma conta
#a conta de origem deve ter saldo suficiente
#Se todas as validações forem atendidas, a transferência deve ser realizada com sucesso.
#3️⃣ Depósito de valores
#Solicitar:
#número da conta
#valor do depósito
#O valor deve ser maior que zero.
#Caso a conta exista, o valor deve ser somado ao saldo.

#4️⃣ Saque de valores
#Solicitar:
#número da conta
#valor do saque
#Regras:

#o valor deve ser maior que zero
#o saldo da conta deve ser suficiente
#Caso contrário, o saque deve ser negado.

#5️⃣ Sair do sistema
#Encerrar a execução do programa exibindo uma mensagem de despedida.

import json
from time import sleep

def leiaInt(msg):
    """
    Lê um valor inteiro digitado pelo usuário.

    Parâmetros:
    msg (str): mensagem exibida ao usuário.

    Retorna:
    int: valor inteiro digitado.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Digite um número inteiro!")


def carregar():
    """
    Carrega as contas bancárias do arquivo banco.json.

    Retorna:
    list: lista de contas carregadas do arquivo.
    """
    contas = []
    try:
        with open("banco.json","r",encoding="utf-8") as arq:
            contas = json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        contas = []
    return contas


def salvar(contas):
    """
    Salva as contas bancárias no arquivo banco.json.

    Parâmetros:
    contas (list): lista de contas bancárias.
    """
    with open("banco.json","w",encoding="utf-8") as arq:
        json.dump(contas,arq)


def linha(txt = 42):
    """
    Cria uma linha de separação.

    Parâmetros:
    txt (int): quantidade de caracteres.

    Retorna:
    str: linha de separação.
    """
    return "-" * txt


def cabecalho(msg):
    """
    Exibe um cabeçalho formatado.

    Parâmetros:
    msg (str): mensagem que será exibida no cabeçalho.
    """
    print(linha())
    print(msg.center(42))
    print(linha())


def listar(contas):
    """
    Lista todas as contas cadastradas.

    Parâmetros:
    contas (list): lista de contas bancárias.
    """
    for conta in contas:
        print(f"{conta['nome']} - {conta['saldo']}R$")


def transferir(origem_num,destinatario_num,saldo,contas):
    """
    Realiza transferência entre duas contas.

    Parâmetros:
    origem_num (int): número da conta de origem.
    destinatario_num (int): número da conta de destino.
    saldo (float): valor da transferência.
    contas (list): lista de contas.

    Retorna:
    str: mensagem informando o resultado da operação.
    """
    origem = None
    destinatario = None
    for conta in contas:
        if conta["numero"] == origem_num:
            origem = conta
        if conta["numero"] == destinatario_num:
            destinatario = conta

    if saldo <=0:
        return f"Erro, Saldo abaixo"
    elif origem == destinatario:
        return f"Erro, não pode ser igual"
    elif origem is None:
        return "Conta de origem vazia"
    elif destinatario is None:
        return "Destinatario vazio!"
    elif origem["saldo"]  < saldo:
        return "Saldo insuficiente"
    else:
        origem["saldo"] -= saldo
        destinatario["saldo"] += saldo
        return  "Transferencia OK"


def deposito(contas,origem_num,saldo):
    """
    Realiza depósito em uma conta.

    Parâmetros:
    contas (list): lista de contas.
    origem_num (int): número da conta.
    saldo (float): valor do depósito.

    Retorna:
    str: mensagem informando o resultado da operação.
    """
    for conta in contas:
        if conta["numero"] == origem_num:
            origem_num = conta
            if saldo >0:
                origem_num["saldo"] += saldo
                return "Deposito OK"
    return "Conta não encontrada"


def sacar_dinheiro(contas,origem_num,sacar):
    """
    Realiza saque de dinheiro de uma conta.

    Parâmetros:
    contas (list): lista de contas.
    origem_num (int): número da conta.
    sacar (float): valor do saque.

    Retorna:
    str: mensagem informando o resultado da operação.
    """
    for conta in contas:
        if conta["numero"] == origem_num:
            origem_num = conta
            if sacar > 0:
                if sacar <= origem_num["saldo"]:
                    origem_num["saldo"] -= sacar
                    return "Saque OK"

    return "Saque nao autorizado"


def main():
    """
    Função principal do sistema bancário.
    Exibe o menu e executa as operações escolhidas pelo usuário.
    """
    contas = carregar()
    if not contas:
        contas = [
            {"numero": 1, "nome": "Rodrigo", "saldo": 500.0,"Ativo": True},
            {"numero": 2, "nome": "Lucas", "saldo": 2000.3,"Ativo":True},
            {"numero": 3, "nome": "Rosineide", "saldo": 54023.1,"Ativo":True},
        ]

    while True:
        cabecalho("Sistema bancário V1")
        print("1 - Listar contas")
        print("2 - Transferencia entre contas")
        print("3 - Depositar valores")
        print("4 - Saque de valores")
        print("5 - Sair do sistema")
        print(linha())

        opc  = leiaInt('Escolha uma opção: ')

        if opc ==1:
            cabecalho("Listando contas...")
            sleep(2)
            listar(contas)

        elif opc == 2:
            cabecalho("Transferencia Bancaria")
            origem_num = leiaInt('Número origem: ')
            destinatario_num = leiaInt('Número destinatário: ')
            saldo = float(input('valor: '))
            transferencia = transferir(origem_num,destinatario_num, saldo, contas)

            print("Efetuando a transferencia . . .")
            sleep(2)

            if transferencia == "Transferencia OK":
                print("Transferencia realizada com sucesso!")
                salvar(contas)
                sleep(2)
            else:
                print("Transferencia não autorizada . . .")
                salvar(contas)
                sleep(2)

        elif opc == 3:
            cabecalho("Depositar valores")
            origem_num = leiaInt('numero: ')
            saldo = float(input('valor: '))
            d = deposito(contas,origem_num,saldo)

            print("Efetuando o deposito . . .")
            sleep(2)

            if d == "Deposito OK":
                print("Deposito realizado com sucesso!")
                salvar(contas)
                sleep(2)
            else:
                print("Deposito não autorizado!")
                sleep(2)

        elif opc == 4:
            cabecalho("Sacar valores")
            origem_num = leiaInt('numero da conta ')
            sacar = float(input('saque: '))
            s = sacar_dinheiro(contas,origem_num,sacar)

            print("EFETUANDO SAQUE . . .")
            sleep(2)

            if s == "Saque OK":
                print("Saque realizado com sucesso")
                sleep(2)
            elif s == "O número é maior que o valor da conta":
                print("Erro, o valor é maior que o saldo atual.")
                sleep(2)
            else:
                print("Saque não autorizado")
                sleep(2)

        elif opc == 5:
            cabecalho("Saindo do sistema . . . Até mais!")
            break

        else:
            print("Valor incorreto! ")

main()



