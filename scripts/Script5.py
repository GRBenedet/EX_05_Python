#O professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('nome do primeiro aluno:')
n2 = input('nome do Segundo aluno:')
n3 = input('nome do terceiro aluno:')
n4 = input('nome do quarto aluno:')

lista = [n1, n2 , n3 , n4]
shuffle(lista)
print('a ordem dos alunos é {}.'.format(lista))