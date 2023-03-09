
# Bibliotecas
from ntpath import join
import os
from posixpath import dirname
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,5)

# Chart config

label = ['LEACH', 'K-means', 'K-medoids']
ordem = [2,1,4]
stringChart = ['-','--','-.']

# label = ['K-means','INTER','INTRA','HOP']
# ordem = [1,2,3,4]
# stringChart = ['-','--','-.',':']

# label = ['K-medoids','INTER','INTRA','HOP']
# ordem = [1,2,3,4]
# stringChart = ['-','--','-.',':']

# label = ['LEACH-INTRA', 'K-means-HOP', 'K-medoids-HOP']
# ordem = [2,1,4]
# stringChart = ['-','--','-.']


# Variáveis
totalSamples = len(label)
qtdNos = 100
qtdRounds = 1700



# Arquivo e Listas
# current_dir = join(os.path.dirname(os.path.realpath(__file__)), 'results')
current_dir = os.path.dirname(os.path.realpath(__file__))

arq = [open(join(current_dir, '00.txt'), 'r'),
       open(join(current_dir, '01.txt'), 'r'),
	   open(join(current_dir, '10.txt'), 'r'),
	   open(join(current_dir, '11.txt'), 'r')]

listaQtdNos = [[],[],[],[]]
listaRounds = [[],[],[],[]]


# Montagem dos Vetores
for k in range(totalSamples):
	cont = 0
	Round = 1
	linha = arq[k].readline()
	while(Round <= qtdRounds):
		if(linha):
			node = linha.split(" ")
			if(Round != int(node[0])):
				listaQtdNos[k].append(cont)
				cont = 0
				Round = int(node[0])
			if(float(node[1]) != 0.0):
				cont = cont + 1
			linha = arq[k].readline()
		else:
			listaQtdNos[k].append(cont)
			Round = Round + 1

	# Construir Vetor de Rounds
	Round = 1
	for num in listaQtdNos[k]:
		#print(str(Round) + " " + str(num))
		listaRounds[k].append(Round)
		Round = Round + 1

	arq[k].close()

for l in range(900):
    for k in range(totalSamples):
        listaRounds[k].append(listaRounds[k][-1] + l)
        listaQtdNos[k].append(0)


# Plot do gráfico
#plt.title('Grafico do Tempo de Vida')
plt.xlabel('Rounds', fontsize=15)
plt.ylabel('Total de sensores vivos', fontsize=15)

plt.axis([0, qtdRounds, -1, qtdNos + 3])
plt.grid(True)

for k in range(totalSamples):
	plt.plot(listaRounds[k], listaQtdNos[k], stringChart[k], label=label[k], zorder=ordem[k])

plt.legend(fontsize=15)


# Configura as margens da imagem
plt.subplots_adjust(left=0.11, bottom=0.11, right=0.96, top=0.96, wspace=None, hspace=None)

plt.savefig('comp_x.png')
plt.show()

