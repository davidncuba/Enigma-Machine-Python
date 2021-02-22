print('-' * 50)
print('╔╦╗       ╔╗╔╗      '.center(50))
print('║╔╬╦╦╦╦═╦╦╣╚╣╚╦═╦═╦╗'.center(50))
print('║╚╣╔╣║║╬║║║╔╣║║╬║║║║'.center(50))
print('╚╩╩╝╠╗║╔╬╗╠═╩╩╩═╩╩═╝'.center(50))
print('    ╚═╩╝╚═╝         '.center(50))
print('-' * 50)

while True:
    abc = {'a': 1, 'b': 2, 'c': 3, 'ç': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13,
           'm': 14,'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24,
           'y': 25, 'z': 26}
    rot = []
    soma = 0
    soma2 = 0
    resulta = ''
    soma3 = 0
    print('krypython'.center(50))
    opcao = input("MENU\n (1) Criptografar\n (2) Descriptografar\nEscolha uma opção valida: ")
    if opcao == '1':
        msg = input('msg: ')
        senha_rot = input('Senha rot?: ')
        while soma != len(msg):
            for letra in senha_rot:
                rot.append(abc[letra] )
            for letraa in range(0, len(msg)):
                resulta = resulta + chr(ord(msg[letraa]) + int(rot[soma2]))
                soma = soma + 1
                soma2 = soma % len(senha_rot)

        with open('tarefa.txt', 'w+') as file:
            file.write(f'{resulta};')

    elif opcao == '2':
        msg = input('msg: ')
        senha_rot = input('Senha rot?: ')
        while soma != len(msg):
            for letra in senha_rot:
                rot.append(abc[letra])
            for letraa in range(0, len(msg)):
                resulta = resulta + chr(ord(msg[letraa]) - int(rot[soma2]))
                soma = soma + 1
                soma2 = soma % len(senha_rot)


    

    print('-' * 50)
    print(resulta)
    print('-' * 50)



