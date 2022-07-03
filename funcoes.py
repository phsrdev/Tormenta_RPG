def continuar(esc=False):
    while esc is not True:
        escolha = input('Prosseguir? (S/N) ').strip().upper()
        if escolha == 'S':
            print('Continuando...')
            return esc == True
        elif escolha == 'N':
            print('Encerrando...')
            return quit()
        while escolha not in 'S' or 'N':
            print('Não entendi, escreva apenas S ou N')
            escolha = input('Prosseguir? (S/N)').strip().upper()
            if escolha == 'S':
                print('Continuando...')
                return esc == True
            elif escolha == 'N':
                print('Encerrando...')
                return quit()


def confirmar(atributo, index):
    escolha = ''
    while escolha not in 'S' or 'N':
        print('Escreva apenas S ou N')
        escolha = input('Deseja Alterar? (S/N)').strip().upper()
        if escolha == 'S':
            print('Continuando...')
            escolha = input('Aumentar ou Diminuir? (+/- ou A/D) ').strip().upper()
            if escolha in '+' or 'A':
                aumenta_atributo(atributo, index, 6)
        elif escolha == 'N':
            print('Voltando')
            break


def mostra_atributo(nome, valor):
    return print(
        f'No momento seus atributos são:\n{nome[0]}: {valor[0]}\n{nome[1]}: {valor[1]}\n{nome[2]}: {valor[2]}\n{nome[3]}: {valor[3]}\n{nome[4]}: {valor[4]}\n{nome[5]}: {valor[5]}')


def criando_atributos(nome, valor):
    o = True
    while o == True or valor[6] > 0:
        print(
            'Para Mostrar atributos(M), Pontos(P), Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C), Sair(Q)')
        x = input('Qual atributo você deseja modificar? ').strip().upper()
        if x == 'F':
            print(f'No momento sua {nome[0]} esta em {valor[0]}')
            confirmar(valor, 0)
        elif x == 'D':
            print(f'No momento sua {nome[1]} esta em {valor[1]}')
            confirmar(valor, 1)
        elif x == 'C':
            print(f'No momento sua {nome[2]} esta em {valor[2]}')
            confirmar(valor, 2)
        elif x == 'I':
            print(f'No momento sua {nome[3]} esta em {valor[3]}')
            confirmar(valor, 3)
        elif x == 'S':
            print(f'No momento sua {nome[4]} esta em {valor[4]}')
            confirmar(valor, 4)
        elif x == 'CA':
            print(f'No momento sua {nome[5]} esta em {valor[5]}')
            confirmar(valor, 5)
        elif x == 'P':
            print(f'No momento você possui {valor[6]} {nome[6]} qual atributo deseja modificar?')
            print('Para Mostrar atributos(M), Pontos(P), Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C), Sair(Q)')
            x = input('O que você deseja? ').strip().upper()
        elif x == 'M':
            mostra_atributo(nome, valor)
        elif x == 'Q':
            return o == False
        elif x not in 'F' or 'D' or 'C' or 'I' or 'S' or 'CA':
            print('Para Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C)')
            x = input('Qual atributo você deseja modificar? ').strip().upper()


def continuar_aumento(esc=False):
    while esc is not True:
        escolha = input('Deseja continuar? (S/N) ').strip().upper()
        if escolha == 'S':
            print('Continuando...')
            return
        elif escolha == 'N':
            print('Encerrando...')
            return True
        while escolha not in 'S' or 'N':
            print('Não entendi, escreva apenas S ou N')
            escolha = input('Deseja continuar? (S/N)').strip().upper()
            if escolha == 'S':
                print('Continuando...')
                return
            elif escolha == 'N':
                print('Encerrando...')
                return True


def aumenta_atributo(atributo, index, index_pontos):
    if 10 >= atributo[index] < 14 and atributo[index_pontos] > 0:
        atributo[index] += 1
        atributo[index_pontos] -= 1
    elif 15 >= atributo[index] < 16 and atributo[index_pontos] > 1:
        atributo[index] += 1
        atributo[index_pontos] -= 2
    elif 16 >= atributo[index] < 18 and atributo[index_pontos] > 2:
        atributo[index] += 1
        atributo[index_pontos] -= 3
    elif atributo[index] >= 18:
        print('Atributo atingiu valor maximo.')
    else:
        print('Você não possui pontos suficientes para aumentar esse atributo.')
        print(f'No momento voce possui {atributo[index_pontos]} pontos.')
    confirmar(atributo, index)
