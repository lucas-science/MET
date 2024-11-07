import subprocess
import time
import csv
import sys
import os
from datetime import datetime

def execute_curl_command():
    # Utilisation de \\ pour échapper correctement le caractère \d dans la commande
    command = "curl -v https://cv-h.phncdn.com/hls/videos/202410/08/458865161/480P_2000K_458865161.mp4/seg-6-v1-a1.ts?Na4uTG22Ka8xWUKi0bZIhxuGHS409HsryAsLa8MOBqDwu0-E4HrDsO-KvNs6vu67nhirTf_d9TnAh0b2nSPOchAnbA2QbQhO5XAaIMLZzWbRMpPgJ5r85bTfxqsxJxG4C_AOQY5sRq0gOzoYwjBgYybv0MRr2VnJwXEN3exJlP_6QKyjuuAtKhqlFleYvlwvSYvaGedHneE 2>&1 | grep -oP '\\d+\\.\\d+\\.\\d+\\.\\d+'"
    
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Décodage en utilisant un encodage plus permissif
    result = stdout.decode('ISO-8859-1')

    # Si on trouve une IP, on la retourne
    ip_address = None
    for line in result.splitlines():
        # Vérification si la ligne contient une adresse IP
        if line.strip():
            ip_address = line.strip()
            break
    
    return ip_address

def write_to_csv(ip_address):
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:')
    file_name = "CDN IP.csv"
    
    file_exists = os.path.isfile(file_name)
    with open(file_name, "a" if file_exists else "w", newline="") as csvfile:
        fieldnames = ['DateTime', 'IP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({'DateTime': timestamp, 'IP': ip_address})

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cdn_analyse.py <interval_minutes>")
        sys.exit(1)

    interval_minutes = int(sys.argv[1])
    
    while True:
        ip_address = execute_curl_command()
        if ip_address:
            write_to_csv(ip_address)
            print(f"IP: {ip_address} written to CSV.")
        else:
            print("No IP found in the curl output.")
        
        print(f"Sleeping for {interval_minutes} minutes...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    main()
