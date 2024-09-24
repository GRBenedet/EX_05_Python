#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

name1 = input('digite o primeiro nome: ')
name2 = input('digite o segundo nome: ')
name3 = input('digite o terceiro nome: ')
name4 = input('digite o quarto nome: ')

lista = [name1 , name2 , name3 , name4]

print('o aluno sorteado foi {}.'.format(choice(lista)))