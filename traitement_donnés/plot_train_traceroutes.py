import networkx as nx
import matplotlib.pyplot as plt
import re
import requests
import subprocess
import time

liste_traceroutes = [[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.9"],
    ["138.197.248.234", "0.0%", "5.7"],
    ["143.244.192.160", "0.0%", "0.6"],
    ["143.244.225.94", "0.0%", "1.4"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "1.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.3"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "2.1"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.6"],
    ["63.243.218.19", "33.3%", "1.6"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "66.7%", "2.2"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "2.5"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "9.8"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "6.1"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.8"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.9"],
    ["138.197.248.232", "0.0%", "3.0"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "2.1"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.3"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "10.5"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "4.5"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.5"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.7"],
    ["138.197.248.234", "0.0%", "1.1"],
    ["143.244.192.160", "0.0%", "0.5"],
    ["143.244.225.94", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.4"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.4"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "1.5"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.5"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "0.0%", "2.1"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.8"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "2.5"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.0"],
    ["138.197.248.232", "0.0%", "1.2"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "2.2"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.8"],
    ["138.197.248.234", "0.0%", "1.1"],
    ["143.244.192.160", "0.0%", "0.5"],
    ["143.244.225.94", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.4"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.4"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "1.5"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.5"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "0.0%", "2.1"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.8"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "2.5"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.0"],
    ["138.197.248.232", "0.0%", "1.2"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "2.2"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.8"],
    ["138.197.248.234", "0.0%", "1.1"],
    ["143.244.192.160", "0.0%", "0.5"],
    ["143.244.225.94", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.4"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.4"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "1.5"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.5"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "0.0%", "2.1"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.8"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "2.5"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.0"],
    ["138.197.248.232", "0.0%", "1.2"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "2.2"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.8"],
    ["138.197.248.234", "0.0%", "1.1"],
    ["143.244.192.160", "0.0%", "0.5"],
    ["143.244.225.94", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.4"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.4"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "1.5"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.5"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "0.0%", "2.1"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.8"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "2.5"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.0"],
    ["138.197.248.232", "0.0%", "1.2"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "2.2"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.8"],
    ["138.197.248.234", "0.0%", "1.1"],
    ["143.244.192.160", "0.0%", "0.5"],
    ["143.244.225.94", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.4"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.4"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "1.5"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.5"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "0.0%", "2.1"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.8"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "2.5"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.0"],
    ["138.197.248.232", "0.0%", "1.2"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "2.2"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.181", "0.0%", "0.8"],
    ["138.197.248.234", "0.0%", "1.1"],
    ["143.244.192.160", "0.0%", "0.5"],
    ["143.244.225.94", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.4"],
    ["if-ae-34-15.tcore3.nto-newyork.as6453.net [66.198.111.59]", "0.0%", "1.4"],
    ["if-ae-22-2.tcore1.nto-newyork.as6453.net [63.243.128.17]", "0.0%", "1.5"],
    ["if-bundle-37-2.qcore1.nto-newyork.as6453.net [63.243.128.145]", "0.0%", "1.5"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["nyk-bb2-link.ip.twelve99.net [62.115.137.14]", "0.0%", "2.1"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.8"],
    ["haproxy-ic-333135.ip.twelve99-cust.net [62.115.12.155]", "0.0%", "2.5"],
    ["cust-reflected-svc11302.ip.reflected.net [64.210.143.161]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
],
[
    ["???", "100.0%", "0.0"],
    ["10.74.132.77", "0.0%", "1.0"],
    ["138.197.248.232", "0.0%", "1.2"],
    ["143.244.192.168", "0.0%", "0.4"],
    ["143.244.225.96", "0.0%", "0.9"],
    ["143.244.225.23", "0.0%", "0.7"],
    ["ix-ae-21-0.tcore3.njy-newark.as6453.net [66.198.70.38]", "0.0%", "0.8"],
    ["if-ae-1-3.tcore4.njy-newark.as6453.net [216.6.57.6]", "0.0%", "1.5"],
    ["???", "100.0%", "0.0"],
    ["???", "100.0%", "0.0"],
    ["63.243.218.19", "0.0%", "1.4"],
    ["???", "100.0%", "0.0"],
    ["nyk-b7-link.ip.twelve99.net [62.115.143.13]", "0.0%", "1.7"],
    ["haproxy-ic-332714.ip.twelve99-cust.net [80.239.160.111]", "0.0%", "2.2"],
    ["cust-reflected-svc11301.ip.reflected.net [64.210.143.160]", "0.0%", "2.6"],
    ["reflectededge.reflected.net [66.254.114.41]", "0.0%", "1.6"]
]
]

def extract_ip(val):
    if ' [216.6.57.6]' in val:
        return '216.6.57.6'
    
    # Regex pour vérifier si la chaîne est une IP simple
    simple_ip_pattern = r"\b\d{1,3}(\.\d{1,3}){3}\b"
    # Regex pour extraire une IP dans une chaîne contenant des crochets
    bracket_ip_pattern = r"\[(\d{1,3}(\.\d{1,3}){3})\]"

    # Si c'est une IP simple, on la retourne telle quelle
    if match := re.search(simple_ip_pattern, val):
        return match.group(0)
    # Sinon, on cherche une IP entre crochets et on la retourne
    elif match := re.search(bracket_ip_pattern, val):
        return match.group(1)
    # Si aucun cas ne correspond, on retourne None ou un message
    else:
        print(val)
        return None
    

def ip_to_city(IP):
    try:
        # Exécute la commande whois et capture la sortie
        result = subprocess.run(["whois", IP], capture_output=True, text=True, check=True)
        
        # Affiche la sortie brute de whois
        
        # Vous pouvez aussi filtrer ou traiter le texte si nécessaire
        # Exemple : pour trouver le pays
        for line in result.stdout.splitlines():
            if "City" in line:
                return line.split(":")[1].strip()
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la commande whois : {e}")
    except FileNotFoundError:
        print("La commande 'whois' n'est pas disponible. Assurez-vous qu'elle est installée.")

def city_to_coordinate(cityName):
    getLoc = loc.geocode(cityName)
    return getLoc.latitude, getLoc.longitude


edges = []
nodes = []

for traceroute in liste_traceroutes:
    for node_index in range(4, len(liste_traceroutes)-1):
        node_1 = traceroute[node_index]
        node_2 = traceroute[node_index+1]
        if '?' in node_1[0] and  '?' in node_2[0]:
            node_1[0] = f'?Hop{node_index}?'
            node_2[0] = f'?Hop{node_index+1}?'
            if node_1[0] not in nodes:
                nodes.append(node_1[0])
            if node_2[0] not in nodes:
                nodes.append(node_2[0])
           
            couple = (node_1[0],node_2[0])
        elif '?' in node_2[0]:
            node_2[0] = f'?Hop{node_index+1}?'
            ip1 = extract_ip(node_1[0])

            if node_2[0] not in nodes:
                nodes.append(node_2[0])
            if ip1 not in nodes:
                nodes.append(ip1)

            couple = (node_1[0],ip2)
        elif '?' in node_1[0]:
            node_1[0] = f'?Hop{node_index}?'
            ip2 = extract_ip(node_2[0])

            if node_1[0] not in nodes:
                nodes.append(node_1[0])
            if ip2 not in nodes:
                nodes.append(ip2)

            couple = (node_1[0],ip2)
        else:
            ip1 = extract_ip(node_1[0])
            ip2 = extract_ip(node_2[0])

            if ip1 not in nodes:
                nodes.append(ip1)
            if ip2 not in nodes:
                nodes.append(ip2)

            couple = (ip1,ip2)
        edges.append(couple)
        
"""

for traceroute in liste_traceroutes:
    for node_index in range(len(traceroute)-1):
        node_1 = traceroute[node_index]
        node_2 = traceroute[node_index+1]
        if '?' not in node_1[0] and '?' not in node_2[0]:
            ip1 = extract_ip(node_1[0])
            ip2 = extract_ip(node_2[0])

            if ip1 not in nodes:
                nodes.append(ip1)
            if ip2 not in nodes:
                nodes.append(ip2)

            couple = (ip1,ip2)
            print(couple)
            edges.append(couple)
"""
G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Affichage du graphe
plt.figure(figsize=(11,6))  # Taille de la figure

pos = nx.spring_layout(G, k=0.1)  # Ajuste k pour augmenter l'espacement
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, 
        font_size=8, font_weight='bold', edge_color='gray', 
        font_color='black', node_shape='o')


# Personnalisation pour rendre le texte plus lisible
plt.title("Graphe des adresses IP", fontsize=16)

plt.savefig("/home/lucas/ecole/3A/projets/MET/traitement_donnés/graphe.png")  # Enregistre le graphe dans un fichier image





