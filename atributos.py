forca = 10
destreza = 10
constituicao = 10
inteligencia = 10
sabedoria = 10
carisma = 10
pontos = 20
def atributos():
    o = True
    while o == True:
        print('Para Força (F), para Destreza (D), para Constituição (C), I')
        x = input('Qual atributo você deseja modificar? ').strip().upper()
        if x not in 'F'