import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ip = '66.254.114.41'
df = pd.read_csv("/home/lucas/ecole/3A/projets/MET/traitement_donnés/data/66.254.114.41_mtr_results.csv")

df_filtered = df[df["Hop"] == 1]

bins_liste = np.linspace(10,15, 50)
df_filtered["PING tot time"].plot(kind='hist', bins=bins_liste, color='skyblue', edgecolor='black')

plt.xlabel("Ping response time [ms]")
plt.ylabel("Number of Pings")
plt.title(f"Ping Response Time Frequency Distribution for\n {ip}")
plt.savefig(f'/home/lucas/ecole/3A/projets/MET/traitement_donnés/ping_time_distribution_{ip}.png')
