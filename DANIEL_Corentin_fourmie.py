import pants
import math
import random
from pprint import pprint
import csv
import networkx as nx
import matplotlib.pyplot as mt

#import des différentes bibliothèques

#création du graph networkx
G = nx.Graph()

#initialisation de la variable pos
pos= ""
i = 0


#ouverture du csv, insertion des edges avec les tenants et aboutissants si ils ne sont pas vide avec le poids de chaque edge correspondant à la distance de la rue en boite aux lettres
with open('VOIES_NM_csv/VOIES_NM.csv','rt') as csvfile:
	fichier = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in fichier:
		i += 1
		print(i)
		if row[6] != "null" and row[6] != "":
			if row[7] != "null" and row[7] != "":
				if row[8] != "null" and row[8] != "":
					if row[10] != "null" and row[10] != "":
						if row[9] != "null" and row[9] != "":
							if row[11] != "null" and row[11] != "":
								debut = row[6]
								fin = row[7]
								poids1 = int((int(int(row[10])-int(row[8]))/2)+1)
								poids2 = int((int(int(row[11])-int(row[9]))/2)+1)
								poids  = max(poids1,poids2)
								label = row[1]
								G.add_edge(debut,fin,weight=poids,label=label)
								pos = nx.spring_layout(G)


#affichage du graph avec networkx

nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edge_labels(G, pos)
nx.draw_networkx(G)

mt.show()


#affichage des rues par lesquelles le chemin est le plus court entre la rue de départ et la rue de fin
print(nx.shortest_path(G, 'LE-PELLERIN Rue Aristide Bertreux','LE-PELLERIN Rue du Huit Mai', weight = 'poids'))


#affichage du poids total du chemin (en boite au lettres)
print(nx.shortest_path_length(G, 'LE-PELLERIN Rue Aristide Bertreux','LE-PELLERIN Rue du Huit Mai', weight = 'poids'))


def fonction(a,b):
    dst=math.sqrt(math.pow(a[1]-b[1],2) + pow(a[0]-b[0],2))
    return dst
    
# création du monde avec les coordonnées des nodes du graph aco-pants

nodes = []
for rue in pos:
	nodes.append((pos[rue][0],pos[rue][1]))

monde = pants.World(nodes,fonction)

#solutions aco-pants

solver = pants.Solver()

##########################################

solution = solver.solve(monde)

print(solution.distance)
print(solution.tour)    # Nodes visited in order
print(solution.path)    # Edges taken in order

###########################################


# OU
"""
##########################################
solutions = solver.solutions(monde)

best = float("inf")
for solution in solutions:
  assert solution.distance < best
  best = solution.distance
  print(best)

##########################################
"""
