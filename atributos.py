
def mostraatributo():
    return print(
        f'No momento seus atributos são:\nForça: {forca}\nDestreza: {destreza}\nConstituição: {constituicao}\nInteligencia: {inteligencia}\nSabedoria: {sabedoria}\nCarisma: {carisma} ')


def criandoatributos():
    o = True
    while o == True or pontos == 0:
        print('Para Mostrar atributos(M), Pontos(P), Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C), Sair(Q)')
        x = input('Qual atributo você deseja modificar? ').strip().upper()
        if x == 'F':
            print(f'No momento sua Força esta em {forca} deseja aumentar?')
            aumentoatributo(forca, pontos)
        elif x == 'D':
            print(f'No momento sua Destreza esta em {destreza} deseja aumentar?')
        elif x == 'C':
            print(f'No momento sua Constituição esta em {constituicao} deseja aumentar?')
        elif x == 'I':
            print(f'No momento sua Inteligencia esta em {inteligencia} deseja aumentar?')
        elif x == 'S':
            print(f'No momento sua Sabedoria esta em {sabedoria} deseja aumentar?')
        elif x == 'C':
            print(f'No momento sua Carisma esta em {carisma} deseja aumentar?')
        elif x == 'P':
            print(f'No momento você possui {pontos} pontos qual atributo deseja modificar?')
            print('Para Pontos(P), Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C)')
            x = input('Qual atributo você deseja modificar? ').strip().upper()
        elif x == 'M':
            mostraatributo()
        elif x == 'Q':
            return o == False
        elif x not in 'F' or 'D' or 'C' or 'I' or 'S' or 'C':
            print('Para Força(F), Destreza(D), Constituição(C), Inteligencia(I), Sabedoria(S), Carisma(C)')
            x = input('Qual atributo você deseja modificar? ').strip().upper()


def continuaraumento(esc=False):
    while esc is not True:
        escolha = input('Deseja continuar? (S/N) ').strip().upper()
        if escolha == 'S':
            print('Continuando...')
            return aumentoatributo()
        elif escolha == 'N':
            print('Encerrando...')
            return True
        while escolha not in 'S' or 'N':
            print('Não entendi, escreva apenas S ou N')
            escolha = input('Deseja continuar? (S/N)').strip().upper()
            if escolha == 'S':
                print('Continuando...')
                return aumentoatributo()
            elif escolha == 'N':
                print('Encerrando...')
                return True


def aumentoatributo(atr, pontos):
    while True:
        if atr < 14:
            atr += 1
            print(f'Aumentou para {atr}')
            pontos -= 1
            print(f'Você ainda possui {pontos}')
            op = input('Deseja continuar? S/N ').strip().upper()
            if op == 'N':
                return False
            elif op == 'S':
                return aumentoatributo(atr, pontos)
        elif 14 <= atr < 16:
            atr += 1
            print(f'Aumentou para {atr}')
            pontos -= 2
            print(f'Você ainda possui {pontos}')
            op = input('Deseja continuar? S/N ').strip().upper()
            if op == 'N':
                return False
            elif op == 'S':
                return aumentoatributo(atr, pontos)
        elif 16 <= atr < 18:
            atr += 1
            print(f'Aumentou para {atr}')
            pontos -= 3
            print(f'Você ainda possui {pontos}')
            op = input('Deseja continuar? S/N ').strip().upper()
            if op == 'N':
                return False
            elif op == 'S':
                return aumentoatributo(atr, pontos)
        elif atr >= 18:
            print(f'Você chegou no valor maximo para {atr}')
            return atr and print(atr)