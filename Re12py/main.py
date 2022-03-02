#Procurando por linhas que comecem com 'X' seguido por qualquer
#caracteres sem espaço em branco ':' seguido por um espaço
#Em seguida imprima o número se for maior que zero.

import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^Details:.*rev=([0-9.]+)', line)
  if len(x) > 0:
    print(x)
    