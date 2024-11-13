import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ip = '67.22.48.3'
type_request = 'Curl' # Curl or Ping

df = pd.read_csv(f"/home/lucas/ecole/3A/projets/MET/traitement_donnés/data/{ip}_mtr_results.csv")
df.drop(df[df['CURL tot time'] > 100].index, inplace=True)
df['DateTime'] = df['DateTime'].str.rstrip(':')
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['half_hour'] = df['DateTime'].dt.floor('45min')

avg_response_time = df.groupby('half_hour')[f'{type_request.upper()} tot time'].mean()

plt.figure(figsize=(11, 6))
avg_response_time.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title(f"Average Response Time for {type_request} \n{ip}")
plt.xlabel("Time Interval")
plt.ylabel("Average Response Time (ms)")
plt.ylim(bottom=0)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(f'/home/lucas/ecole/3A/projets/MET/traitement_donnés/{type_request}_reqTime_over_time_{ip}.png')

