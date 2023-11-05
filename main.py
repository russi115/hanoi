import os

from pila import Pila
from time import sleep

def hanoi(n, origen, auxiliar, destino):
	if n==1:
		mover_disco(origen-1, destino-1)
	else:
		hanoi(n-1, origen, destino, auxiliar)
		mover_disco(origen-1, destino-1)
		hanoi(n-1,auxiliar,origen,destino)

def crea_discos(n):
	torre=[[]]
	copia_n=n

	for i in range(2*n+3):
		if i==(2*n+3)//2:
			torre[0].append("|")
		else:
			torre[0].append(" ")

	for i in range(1, n+1):
		torre.append([])
		for j in range(2*n+3):
			if j < copia_n-1 or j > (2*i+copia_n+1):
				torre[i].append(" ")
			elif j==copia_n-1:
				torre[i].append("[")
			elif j==(2*i+copia_n+1):
				torre[i].append("]")
			else:
				torre[i].append("=")
		copia_n-=1

	return torre

def mover_disco(origen, destino):
	pintar_torres()
	dato=pilas[origen].desapilar()
	pilas[destino].apilar(dato)
	print()
	sleep(0.01)

def pintar_torres():

	os.system("cls")
	#os.system("clear")

	for i in range(n, -1, -1):
		for j in range(3):
			dibujar_discos(pilas[j].items[i])
		print()

def dibujar_discos(noDisco):
	for i in torre[noDisco]:
		print(i, end="")

def llenar_pilas(n):
	for i in range(n,-1,-1):
		pilas[0].apilar(i)
		pilas[1].apilar(0)
		pilas[2].apilar(0)

	pilas[0].puntero=n
	pilas[1].puntero=0
	pilas[2].puntero=0



n=int(input("cantidad de discos: \n"))
torre = crea_discos(n)

pilas=[Pila(),Pila(), Pila()]

llenar_pilas(n)
hanoi(n,1,2,3)
pintar_torres()