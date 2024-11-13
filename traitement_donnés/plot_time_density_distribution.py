import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger le DataFrame
ip = '66.254.114.41'
type_req = 'Ping' # Curl or Ping
df = pd.read_csv("/home/lucas/ecole/3A/projets/MET/traitement_donnés/data/66.254.114.41_mtr_results.csv")

# Filtrer pour l'hop 1
df_filtered = df[df["Hop"] == 1]

# Extraire les temps de réponse Ping
ping_times = df_filtered[f"{type_req.upper()} tot time"]

# Calculer les statistiques de la distribution réelle
mean_ping = ping_times.mean()
std_ping = ping_times.std()

# Créer les bins pour l'histogramme
bins_liste = np.linspace(10, 14.5, 50)

# Calculer l'histogramme
hist, bin_edges = np.histogram(ping_times, bins=bins_liste, density=True)

# Calculer la CDF en utilisant la méthode cumsum pour la fonction de répartition
cdf = np.cumsum(hist) * np.diff(bin_edges)[0]  # Multiplier par la largeur des bins pour la normalisation
print(cdf)
# Tracer la CDF
plt.figure(figsize=(10, 6))
plt.plot(bin_edges[1:], cdf, marker='o', linestyle='-', color='skyblue', label='CDF réelle')

# Ajouter des étiquettes et un titre
plt.xlabel(f"{type_req} response time [ms]")
plt.ylabel("Cumulative Probability")
plt.title(f"{type_req} Response Time CDF for {ip}")
plt.legend()

# Sauvegarder le graphique
plt.savefig(f'/home/lucas/ecole/3A/projets/MET/traitement_donnés/cdf_{type_req}_time_{ip}.png')

