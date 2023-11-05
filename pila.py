class Pila:
		"""Clase personalizada de la estructura Pila"""
		
		def __init__(self):
			self.items = []
			self.puntero=0

		def apilar(self, x):
			self.items.insert(self.puntero,x)
			self.puntero=self.puntero+1

		def desapilar(self):
			try:
				self.puntero=self.puntero-1
				copiaItems= self.items[self.puntero]
				self.items[self.puntero]=0
				return copiaItems
			except:
				print("La pila esta vacia")

		def es_vacia(self):
			return self.items==[]			
