import math as mat

class Calculadora:
	def __init__(self):
		self._resultado = 0

	def somar(self, valor):
		self._resultado += valor

	def subtrair(self, valor):
		self._resultado -= valor

	def multiplicar(self, valor):
		self._resultado *= valor
	def sqrt(self, valor):
		self._resultado += mat.sqrt(valor)

	def dividir(self, valor):
		if valor != 0:
			self._resultado /= valor
		else:
			print("Erro: Divisão por zero não é permitida.")

	def get_resultado(self):
		return self._resultado

	def reset(self):
		self._resultado = 0

calc = Calculadora()
'''calc.somar(10)
calc.subtrair(2)
calc.multiplicar(3)
calc.dividir(4)
calc.sqrt(666)'''
calc.sqrt(666)
print(calc.get_resultado())  # Saída: 6.0
calc.reset()