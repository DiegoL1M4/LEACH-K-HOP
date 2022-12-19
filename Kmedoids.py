import math
import numpy as np

class K_medoids:

    def calcDistance(point1, point2):
        total = 0
        for coord in range(len(point1)):
            total += math.pow(point2[coord] - point1[coord], 2)
        return math.sqrt(total)

    def exec(CH, nodes, movements):
        # Movement cycle
        for k in range(movements):
            # Definition of Centroids
            for node in nodes:
                distance = ''
                for nodeCH in CH:
                    distanceCalc = K_medoids.calcDistance([node[2], node[3]], [nodeCH[2], nodeCH[3]])
                    if(distance == '' or distanceCalc < distance):
                        distance = distanceCalc
                        # node[7] = centroids.index(centroid)
                        node[7] = nodeCH
        
        
            # Calc new centroids
            collection = []
            sortedNodes = sorted(nodes, key=lambda node: node[7])
            currentCH = sortedNodes[0][7]
        
            centroids = []
            for node in sortedNodes:
                if(currentCH != node[7]):
                    centroids.append([np.mean(collection, axis=0).tolist(), []])
                    currentCH = node[7]
                    collection = []
                collection.append([node[2], node[3]])
            centroids.append([np.mean(collection, axis=0).tolist(), []])

            # Reset Nodes Config
            for node in CH:
                node[6] = 0
                nodes.append(node)
            CH = []

            for node in nodes:
                node[7] = []

            # Select nearest node
            for centroid in centroids:
                distance = ''
                for node in nodes:
                    if(node[6] != 1):
                        distanceCalc = K_medoids.calcDistance(centroid[0], [node[2], node[3]])
                        if(distance == '' or distanceCalc < distance):
                            distance = distanceCalc
                            centroid[1] = node

            for centroid in centroids:
                if(centroid[1][6] == 0):
                    nodes.remove(centroid[1])
                    centroid[1][6] = 1
                    CH.append(centroid[1])
                
        return CH
        