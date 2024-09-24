#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um número: '))

print('O Número digitado foi {} e sua porcão inteira é {}.'.format(num , trunc(num)))