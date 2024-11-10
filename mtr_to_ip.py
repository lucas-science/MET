import csv
import subprocess
import os
import socket
from datetime import datetime
import requests
import time
import re
import sys

def run_mtr_command(command):
    """Exécute la commande mtr et renvoie la sortie."""
    try:
        # Exécution de la commande mtr
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
        return None

def get_Domain_Name(IP):
    try:
        hostname = socket.gethostbyaddr(IP)[0]
        return hostname
    except socket.herror:
        return "?"

def get_ping_time(host):
    command = f"ping -c 4 {host}"
    result = os.popen(command).read()
    if "time=" in result:
        start = result.rfind("time=")
        if start != -1:
            end = result.find(" ", start)
            return float(result[start + 5:end])
    return "Ping failed"

def get_curl_time(host):
    try:
        start_time = time.time()
        response = requests.get(f'http://{host}')
        elapsed_time = (time.time() - start_time) * 1000
        return elapsed_time
    except requests.exceptions.RequestException as e:
        return "Erreur dans la requête"
    
def add_data_to_csv_file(output, filName, ip):
    file_exists = os.path.isfile(filName)
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:')

    with open(filName, "a" if file_exists else "w", newline="") as csvfile:
        fieldnames = ['DateTime', 'Hop', 'IP', 'Domain Name', 'Loss%', 'Sent', 'Last', 'Avg', 'Best', 'Worst', 'StDev', 'PING tot time', 'CURL tot time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        
        curl_time = get_curl_time(ip)
        ping_time = get_ping_time(ip)

        for line in output.splitlines():
            if line.startswith(" "):
                columns = line.split()
                ip_node = columns[1]
                if ip_node != '???':
                    domain_name = get_Domain_Name(ip_node)
                else:
                    domain_name = '???'
                if len(columns) > 7: 
                    writer.writerow({
                        'DateTime': timestamp,
                        'Hop': columns[0].strip('.|--'),
                        'IP': columns[1],
                        'Domain Name': domain_name,
                        'Loss%': columns[2],
                        'Sent': columns[3],
                        'Last': columns[4],
                        'Avg': columns[5],
                        'Best': columns[6],
                        'Worst': columns[7],
                        'StDev': columns[8],
                        'PING tot time': ping_time,
                        'CURL tot time': curl_time
                    })

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 mtr_to_ip.py <IP_address> <interval_minutes>")
        sys.exit(1)

    ip_address = sys.argv[1]
    interval_minutes = int(sys.argv[2])
    
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        print(f"L'adresse IP '{ip_address}' n'est pas valide.")
        sys.exit(1)

    command = f"mtr --report --report-cycles=10 -b -n {ip_address}"

    while True:
        output = run_mtr_command(command)
        if output:
            add_data_to_csv_file(output, f"{ip_address}_mtr_results.csv", ip_address)
        print(f"Data collected for {ip_address}. Sleeping for {interval_minutes} minutes...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    main()
