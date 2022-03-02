# Procure por linhas que comecem com 'Detalhes: rev='
# seguido por números e '.'
# Em seguida, imprima o número se for maior que zero
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^X\S*: ([0-9.]+)', line)
  if len(x) > 0:
    print(x)