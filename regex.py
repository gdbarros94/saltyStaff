import re

def validar_texto(texto):
  padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
  return bool(re.match(padrao, texto))

# Exemplos de uso:

texto3 = "Texto com, vírgulas"

print(validar_texto(texto1))  # True
print(validar_texto(texto2))  # False
print(validar_texto(texto3))  # True