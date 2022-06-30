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
            print(f'No momento sua {nome[0]} esta em {valor[0]} deseja aumentar?')
        elif x == 'D':
            print(f'No momento sua {nome[1]} esta em {valor[1]} deseja aumentar?')
        elif x == 'C':
            print(f'No momento sua {nome[2]} esta em {valor[2]} deseja aumentar?')
        elif x == 'I':
            print(f'No momento sua {nome[3]} esta em {valor[3]} deseja aumentar?')
        elif x == 'S':
            print(f'No momento sua {nome[4]} esta em {valor[4]} deseja aumentar?')
        elif x == 'CA':
            print(f'No momento sua {nome[5]} esta em {valor[5]} deseja aumentar?')
        elif x == 'P':
            print(f'No momento você possui {valor[6]} {nome[6]} qual atributo deseja modificar?')
            print('Para Pontos(P), Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C)')
            x = input('Qual atributo você deseja modificar? ').strip().upper()
        elif x == 'M':
            mostraatributo(nome, valor)
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
    atributo[index] += 1
    atributo[index_pontos] -= 1
