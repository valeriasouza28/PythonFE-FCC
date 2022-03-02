#Encontrar linhas que comcomecem De e com um caractere
# Seguido por um número de dois digitos entre 00 e 99 e seguido por ":"
# Em seguida imprima o número se for maior que zero

import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^From .* ([0-9][0-9]):', line)
  if len(x) > 0: print(x)
  