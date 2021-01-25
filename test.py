import requests

x = requests.Request('GET', 'https://w3schools.com/python/demopage.htm')

print(x.prepare())