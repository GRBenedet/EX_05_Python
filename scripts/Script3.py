#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('digite um angulo: '))

print('O cosseno é {:.2f}. \nA tangente é {:.2f}. \nO seno é {:.2f}.'.format(math.cos(math.radians(ang)) , math.tan(math.radians(ang)) , math.sin(math.radians(ang))))