import socket

import requests
from scapy.all import traceroute

'''
if you want to know the path/route that ur packet travels over internet just execute this code and enter the domain name.

sample output for each hop
Geolocation: {'ip': '142.250.199.142', 'hostname': 'bom07s36-in-f14.1e100.net', 'city': 'Mumbai', 
'region': 'Maharashtra', 'country': 'IN', 'loc': '19.0728,72.8826', 'org': 'AS15169 Google LLC', 
'postal': '400017', 'timezone': 'Asia/Kolkata'}
# IPinfo API token (replace with your actual token its very easy, just login and go to token)
'''
IPINFO_API_TOKEN = 'your ipinfo api token'

def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json?token={IPINFO_API_TOKEN}")
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error retrieving geolocation for IP {ip}: {e}")
        return {'ip': ip, 'city': 'Unknown', 'region': 'Unknown', 'country': 'Unknown'}


def main():
    domain = input("Enter a domain name: ")
    try:
        destination_ip = socket.gethostbyname(domain)
        print(f"Destination IP: {destination_ip}")

        result, _ = traceroute(destination_ip)

        visited_ips = set()

        for snd, rcv in result:
            
            hop_ip = rcv.src

            # Check for Anycast IP
            if hop_ip not in visited_ips:
                visited_ips.add(hop_ip)
                geolocation = get_geolocation(hop_ip)
                anycast = geolocation.get('anycast', False)
                print(f"IP: {hop_ip}")
                if anycast:
                    print(f"  (Anycast IP)")
                print(f"Geolocation: {geolocation}")

    except PermissionError:
        print("Permission denied: Make sure to run the script with elevated privileges (sudo).")

if __name__ == "__main__":
    main()
