#Procure por linhas que tenham um sinal de arroba entre os caracteres
#Os caracteres devem ser uma letra ou um número
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
  if len(x) > 0:
    print(x)

# Code: py4e.com/code3/re0.py
