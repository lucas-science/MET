import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Charger les données
ip = '66.254.114.41'
df = pd.read_csv(f"/home/lucas/ecole/3A/projets/MET/traitement_donnés/data/{ip}_mtr_results.csv")

paths = []
current_path = []

for idx, row in df.iterrows():
    hop, ip = row['Hop'], row['IP']
    
    # Vérifier si le hop est 1, indiquant un nouveau paquet
    if hop == 1 and current_path:
        paths.append(current_path)  # Ajouter le paquet actuel à la liste
        current_path = []  # Réinitialiser pour le nouveau paquet
    
    current_path.append(ip)  # Ajouter l'IP au paquet actuel

# Ajouter le dernier paquet s'il reste des éléments
if current_path:
    paths.append(current_path)


edges = []

for path in paths:
    for i, node in enumerate(path):
        if node == '???':
            path[i] = f'?HOP-{i}'

# Créer le graphe orienté et ajouter les nœuds et arêtes
G = nx.DiGraph()  # Utiliser un graphe orienté
for path in paths:
    for i in range(len(path) - 1):
        couple = (path[i], path[i + 1])  # Utiliser des tuples pour les arêtes orientées
        if couple not in edges:
            edges.append(couple)
        
# Dessin du graphe
G.add_edges_from(edges)
# Disposition initiale avec spring_layout
pos = nx.spring_layout(G, k=3, iterations=1000)

node1, node2 = '192.168.1.254', '66.254.114.41'
force_strength = 0.4

direction_vector = np.array(pos[node2]) - np.array(pos[node1])
norm = np.linalg.norm(direction_vector)

if norm > 0:
    direction_vector = direction_vector / norm  # Normaliser le vecteur
    pos[node1] = pos[node1] - force_strength * direction_vector  # Déplacer node1 dans la direction opposée
    pos[node2] = pos[node2] + force_strength * direction_vector  # Déplacer node2 dans la direction

plt.figure(figsize=(20,5))
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray", arrowsize=20)
plt.title("Graphe orienté avec force de répulsion entre les nœuds spécifiés")
plt.savefig(f"/home/lucas/ecole/3A/projets/MET/traitement_donnés/{ip}_traceroute.png")
