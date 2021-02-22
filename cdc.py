def SalvaMensagem(resultado):
    with open('senhascdc.txt', 'a+') as file:
        file.write(f'{resultado};')
    print('Salvo com sucesso')

def MensagensCriptografadas():
    with open('senhascdc.txt', 'r') as file:
        mensagens = file.read()
        mensagens = mensagens.split(';')
        for mensagem in mensagens:
            if mensagem != '':
                print(mensagens.index(mensagem), mensagem)
        return mensagens

while True:
    # Variável aqui para iniciar limpo
    resultado = ''

    print('Codigo De Cesar 2.0'.center(50))
    print('-' * 50)
    opcao = input("MENU\n (1) Criptografar\n (2) Descriptografar\nEscolha uma opção valida: ")
    if opcao == '1':
        msg = input("Digite sua mensagem: ")
        rot = int(input('Quantia de rot?: '))

        # Faça isso para cada letra da mensagem digitada
        for letra in range(0, len(msg)):
            # Variável recebe ela mesmo e a soma de uma letra da mensagem com o rot
            # Para fazer a soma paga o código numérico da letra e faz a soma, depois é só transformar em letra novamente
            resultado = resultado + chr(ord(msg[letra]) + rot)
        SalvaMensagem(resultado)
            
    # A opção 2 é a mesma coisa, só que ao invés de somar ela subtrai o rot
    elif opcao == '2':
        # 
        mensagens = MensagensCriptografadas()
        msg = int(input("Digite o código da mensagem criptografada: "))
        msg = mensagens[msg]
        rot = int(input('Quantia de rot?: '))

        for letra in range(0, len(msg)):
            resultado = resultado + chr(ord(msg[letra]) - rot)

    print('-' * 50)
    print(resultado)
    print('-' * 50)