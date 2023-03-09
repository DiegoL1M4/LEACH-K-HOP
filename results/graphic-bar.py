# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Define o tamanho da imagem
plt.rcParams['figure.figsize'] = (6,5)

for op in [1,2]:
    if(op == 1):
        #''' K-means
        # HOP = [cenário1,cenário2,cenário3, ...]
        H00 = [1051.42]
        H01 = [1044.15]
        H10 = [1287.42]
        H11 = [1218.51]
        # cenario = [00,01,10,11]
        cen1 = [21.55, 17.32, 16.15, 8.30]
        #'''
    if(op == 2):
        #''' K-medoids
        # HOP = [cenário1,cenário2,cenário3, ...]
        H00 = [1042.48]
        H01 = [1024.66]
        H10 = [1297.78]
        H11 = [1221.15]
        # cenario = [00,01,10,11]
        cen1 = [16.89, 15.28, 13.78, 6.52]
        #'''

    barWidth = 0.85 #4legendas

    r1 = np.arange(4)

    capsizevar = 20

    plt.bar(r1, 
        [H00[0],H01[0],H10[0],H11[0]], 
        width=barWidth, yerr=cen1, 
        capsize=capsizevar, 
        color = ['lightcoral', 'steelblue', 'c', 'lightskyblue'])
    
    ajuste = -0.5

    if(op == 1):
        plt.xticks([r + barWidth+ajuste -0.35 for r in range(4)], ['K-means','INTER','INTRA','HOP'], fontsize=15)
    if(op == 2):
        plt.xticks([r + barWidth+ajuste -0.35 for r in range(4)], ['K-medoids','INTER','INTRA','HOP'], fontsize=15)

    plt.ylabel('Quantidade de Frames', fontsize=15)
    #plt.title('Clustering')

    plt.grid(True)

    # Configura as margens da imagem
    plt.subplots_adjust(left=0.13, bottom=0.08, right=0.96, top=0.95, wspace=None, hspace=None)

    if(op == 1):
        plt.savefig('k-means-bar.png')
    elif(op == 2):
        plt.savefig('k-medoids-bar.png')

    #plt.show()
    plt.clf()

'''
# Montagem da Dispersão
arq = open('nodes.txt', 'r')
linha = arq.readline()

fig, ax = plt.subplots()
ax.bar(10, 15)
ax.annotate("Maior valor",
            xy=(10, 12),
            xycoords='data',
            xytext=(11, 10),
            textcoords='data')
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
plt.show()

plt.axis([-3, 135, -3, 103])

'''
