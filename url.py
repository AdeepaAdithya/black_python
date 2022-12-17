import requests
import socket
import urllib.request
z = input("Enter the url")

hostname = z
hostname_ip = socket.gethostbyname(hostname)
print(hostname_ip)



r = requests.get("https://"+z)
print(r.headers)
with urllib.request.urlopen("https://"+z) as a:
    h = a.read()
print(h)

