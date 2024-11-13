import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
ip = '66.254.114.41'
df = pd.read_csv(f"/home/lucas/ecole/3A/projets/MET/traitement_donnés/data/{ip}_mtr_results.csv")

# Remplacer les IP égales à '???' par '?Hop-index_du_Hop'
df['IP'] = df.apply(lambda row: f"?Hop-{row['Hop']}" if row['IP'] == '???' else row['IP'], axis=1)

# Enlever le signe '%' et convertir la colonne 'Loss%' en float
df['Loss%'] = df['Loss%'].str.replace('%', '').astype(float)

# Calculer la moyenne des pertes par 'Hop'
group_by_hop = df.groupby('IP')
mean_loss_by_hop = group_by_hop['Loss%'].mean()

# Tracer un graphique à barres
ax = mean_loss_by_hop.plot(kind='bar', color='skyblue', edgecolor='black')

# Ajuster l'axe des ordonnées pour avoir des pourcentages (0 à 100)
ax.set_ylabel('Loss (%)')  # Label de l'axe Y
ax.set_ylim(0, 100)  # Limite de l'axe Y entre 0 et 100%  # Ticks en pourcentage

# Titre et labels des axes
ax.set_title(f"Loss distribution by Hop ({ip})")
ax.set_xlabel('Hop index')
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right", fontsize=7)

# Sauvegarder le graphique
plt.savefig(f'/home/lucas/ecole/3A/projets/MET/traitement_donnés/loss_distribution_by_hop_{ip}.png')
