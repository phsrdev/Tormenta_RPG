def prosseguir(esc=False):
    while esc is not True:
        escolha = input('Podemos Prosseguir? (S/N) ').strip().upper()
        if escolha == 'S':
            print('Continuando...')
            return esc == True
        elif escolha == 'N':
            print('Encerrando...')
            return quit()
        while escolha not in 'S' or 'N':
            print('Não entendi, escreva apenas S ou N')
            escolha = input('Podemos Prosseguir? (S/N)').strip().upper()
            if escolha == 'S':
                print('Continuando...')
                return esc == True
            elif escolha == 'N':
                print('Encerrando...')
                return quit()
