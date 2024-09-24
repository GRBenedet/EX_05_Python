#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

c1 = float(input('qual o tamanho do cateto oposto? '))
c2 = float(input('Qual o tamanho do cateto adjacente? '))

print('A hipotenusa vai medir {:.2f}.'.format(hypot(c1 , c2)))