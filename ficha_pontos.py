# Projeto tormenta iniciado 28/06/2022, projeto inicial criação de fichas.
import config
import atributos as at
import funcoes as fc
import config as cf
print('Olá, estou aqui para te ajudar a criar sua ficha Tormenta 20.')
print('Vamos começar escolhendo seus atributos iniciais.')
print('Iremos usar o metodo de Geração por Pontos.')
print('Em vez de rolar, você irá comprar seus atributos com pontos. Neste caso, possui 20 pontos para gastar, conforme a tabela ao lado. Este método permite maior controle por parte dos jogadores e evita heróis desequilibrados, além de permitir a construção de personagens sem a presença do mestre.')
fc.continuar()
at.aumenta_atributo(cf.valor_atributos, 0, 6)
print(cf.valor_atributos)
print('Atributos por Pontos ')
print('Valor de Atributo Custo\n8            2 pontos\n9             1 ponto\n10            0 ponto\n11            1 ponto\n12           2 pontos\n13           3 pontos\n14           4 pontos\n15           6 pontos\n16           8 pontos\n17          11 pontos\n18          14 pontos')
fc.continuar()
at.mostra_atributo(cf.nome_atributos, cf.valor_atributos)
print(cf.valor_atributos[0], cf.valor_atributos[6])
at.criando_atributos(cf.nome_atributos, cf.valor_atributos)














