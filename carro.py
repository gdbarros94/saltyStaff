class Carro:
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.__modelo = modelo
		self.ano = ano
		
	def acelerar(self):
		print(f"O {self.ano} está acelerando.")

	def frear(self):
		print(f"O {self.__modelo} está freando.")

# Criando um objeto da classe Carro
meu_carro = Carro(marca="Toyota", ano=2020, modelo="Corolla")
#meu_carro.acelerar()  # Saída: O Corolla está acelerando.
outro_carro = Carro("vw", "gol", 2020)
outro_carro.frear()
#print(outro_carro.__modelo)